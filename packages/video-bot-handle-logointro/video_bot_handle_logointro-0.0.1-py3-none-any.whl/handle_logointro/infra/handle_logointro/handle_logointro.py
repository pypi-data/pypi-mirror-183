from os import path 

from handle_logointro.utils.helpers import get_attr
from handle_logointro.infra.script import Script

from handle_logointro.models.page import Section
from handle_logointro.models.saved_file import SavedFile
from handle_logointro.models.video import MyVideo 

from handle_logointro.utils.helpers import generate_id
from handle_logointro.utils.video import get_video_duration

from handle_logointro.models.logointro import LogoIntro

SCRIPT_NAME = "HANDLE LOGO INTROS"
NO_DATA  = "No Sections" 
ERROR_SCRIPT = "Could not handle logo intro"

class HandleLogoIntro(Script):
   
    def __init__(self, config, text_robot, logger = None):
        
        super().__init__(SCRIPT_NAME, logger)

        self.config = config
        
        self.on_lambda = get_attr(self.config, 'on_lambda', False)
        self.data = get_attr(self.config, 'data', {})
        self.temp_directory = get_attr(self.config, 'temp_directory', '/tmp')

        self.minimal_frequency = get_attr(self.config, 'minimal_frequency', 1)
        self.moderate_frequency = get_attr(self.config, 'moderate_frequency', 2)
        self.agressive_frequency = get_attr(self.config, 'agressive_frequency', 3)
        self.minimal_content_time_seconds = get_attr(self.config, 'minimal_content_time_seconds', 30)

        self.ad_mode = get_attr(self.config, 'ad_mode', 1)

        self.logointro_text = get_attr(self.config, 'logointro_text', '')

        self.text_robot = text_robot

        

   


       
    






    












    
    

         
