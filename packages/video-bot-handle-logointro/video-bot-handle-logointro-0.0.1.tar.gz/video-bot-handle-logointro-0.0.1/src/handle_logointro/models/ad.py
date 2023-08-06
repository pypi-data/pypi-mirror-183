class Ad:
     def __init__(self, 
                path = None,
                media_id = None,
                path_converted = None,
                media_type = None,
                time = None, 
                ad_video_time = None,
                attributions = None) -> None:
        
        

        self.path = path
        self.path_converted = path_converted
        self.time = time
        self.ad_video_time = ad_video_time
        self.media_id = media_id
        self.attributions = attributions
        self.media_type = media_type