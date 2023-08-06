from os import path
from telnetlib import EXOPL
from handle_logointro.services.base_service import BaseService
from handle_logointro.utils.helpers import get_attr, generate_id, set_attr
from handle_logointro.utils.json import  from_json
from handle_logointro.utils.file import read_binary_file
from handle_logointro.utils.video import get_video_duration
from handle_logointro.models.page import Sentence
from handle_logointro.models.logointro import LogoIntro


class HandleLogoIntroService(BaseService):

            
    def replace_placeholders(self, text):
        new_text = text
        channel_name = get_attr(self.channel_info, 'name', '')
        new_text = str(new_text).replace("{{channel_name}}", f"{channel_name}")  
        return new_text   
    

    
    def get_service(self, external_services, type):
        services = list(filter(lambda service: service['type'] == type, external_services))
        if (len(services) == 0):
            raise Exception('external service of type ' + type + ' must be injected to the main service' )
        else:
            return services[0]['instance']    

    def __init__(self, config, executer, downloader, saver, external_services = []):

        self.config = config

        self.channel_info = get_attr(self.config, "channel_info", {})

        self.use_subtitles = get_attr(self.channel_info,  'use_subtitles', True)
        self.use_narration = get_attr(self.channel_info,  'use_narration', True)
        self.logointro_muted = get_attr(self.channel_info,  'logointro_muted', False)

        self.logointro_text = get_attr(self.config,  'logointro_text', '')
        self.ovewrite_time = get_attr(self.config,  'ovewrite_time', 0)

        self.logo_intro_video_source = get_attr(self.config,  'logo_intro_video_source', None)
        self.logo_intro_file_source = get_attr(self.config,  'logo_intro_file_source', None)

        if (self.logo_intro_video_source == None):
            raise Exception('Logo intro video is required (key = "logo_intro_video_source")')

        if (self.logo_intro_file_source == None):
            raise Exception('Logo intro file is required (key = "logo_intro_file_source")')    

        #workers
        self.executer = executer
        self.downloader = downloader
        self.saver = saver

        self.speech_service = self.get_service(external_services, 'speech')
        self.time_service = self.get_service(external_services, 'add-time')
        self.text_utils_service = self.get_service(external_services, 'text-utils')

        self.temp_directory =   get_attr(self.config,  'temp_directory', '/tmp')
        self.ads =   get_attr(self.config,  'ads', [])

    
    def handle_logointro(self, file_object):

        file_path = file_object['file']
        sentences = []
        sentence = None

        if (self.ovewrite_time != 0):
            video_time = self.ovewrite_time
        else:    
            video_time = get_video_duration(file_path)

        

        #add sentence
        
        if (len(str(self.logointro_text)) > 0):
            text = self.replace_placeholders(self.logointro_text)                
            sentence = Sentence(media_id = None, id = generate_id(),text=text,
                                keywords=None,subtitles=None,speech=None,time=video_time)
        
        if (sentence != None):

            #add keywords to sentence
            keywords = self.text_utils_service.extract_keywords(sentence)
            sentence.keywords = keywords

            #add subtitles to sentence
            if (self.use_subtitles == True ):
                subtitles = self.text_utils_service.generate_subtitles_for_sentence(sentence)
                sentence.subtitles = subtitles

            #add speech to sentence
            if ((self.use_narration == True )  and (self.logointro_muted == False) ): 
                speech = self.speech_service.get_speech_for_sentence(sentence)
                sentence.speech = speech

            #temporary - for quick test    
            #sentence.speech = from_json('./model.json')


            #download files from s3/mongo when necessary
            binary_files = []
            download_required, downloaded_files = self.download_speech_files(sentence)
            if (download_required):
                
                #change the path of the file
                set_attr(sentence.speech, 'file', downloaded_files[0] )
                binary_files = self.read_binary_files(downloaded_files)

                #add times to sentence
                sentence =  self.time_service.get_time_to_sentence(sentence, binary_files[0])

            else:
                #add times to sentence
                sentence =  self.time_service.get_time_to_sentence(sentence)


            sentences.append(sentence)


        logointro =  LogoIntro(media_id = generate_id(), path = file_path, path_converted = '', 
                                logo_video = file_object,
                                video_time = video_time, 
                                logo = None,
                                sentences = sentences)

        return logointro    



    def read_binary_files(self, files):
        binary_downloaded_files = []
        for file in files:
            binary_downloaded_files.append(read_binary_file(file))
        return binary_downloaded_files

    def download_speech_files(self, sentence):
        download_required = False
        downloaded_files = []
        

        #if speech exists and file is remote, download it before:
        speech = get_attr(sentence, 'speech', {})
        if (speech != None):
            source = get_attr(speech, 'source', {})
            if (source != None):
                source_bucket = get_attr(source, 'bucket_name',None)
                if (source_bucket != None): 
                    directory = path.dirname(source['file_path'])
                    file = source['file_id']
                    download_source = {'source_bucket' : source_bucket, "sources": [{ "directory": directory, "objects": [file] }]}
                    self.downloader.reset_sources()
                    self.downloader.add_sources(download_source)
                    download_results, downloaded_files = self.downloader.run()
                    download_required = True
                    if (len(downloaded_files) == 0):
                        raise Exception('download is required,but could not download files from s3 bucket')
                  

                else:
                    download_required = False
                    downloaded_files = [] 
            else:
                download_required = False
                downloaded_files = [] 

        else:
            download_required = False
            downloaded_files = []

        return (download_required, downloaded_files)      


    def copy_logo_source(self, source):
        
        downloaded_files = []
        download_results = []
        saved_files = []

        source_bucket = get_attr(source,'source_bucket', '' )
        source = get_attr(source,'source', {} )
        directory = get_attr(source,'directory', '')
        objects = get_attr(source,'objects', [])
        file = objects[0]

        download_source = {'source_bucket' : source_bucket, "sources": [{ "directory": directory, "objects": [file] }]}
        self.downloader.reset_sources()
        self.downloader.add_sources(download_source)

        download_results, downloaded_files = self.downloader.run()
        if (len(downloaded_files) > 0):
            saved_files = self.saver.run(downloaded_files)    

        return saved_files

    def execute(self):
       
        logointro = None        
        
        #logo intro video source
        saved_files = self.copy_logo_source(self.logo_intro_video_source)

        #convert files to thumbs
        if (len(saved_files) > 0):
             logointro  = self.handle_logointro(saved_files[0])        

        #logo intro file source     
        saved_logo_files = self.copy_logo_source(self.logo_intro_file_source)
        if (len(saved_logo_files) > 0):
            logointro.logo = saved_logo_files[0]
        
        return logointro

        
       
      