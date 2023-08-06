from os import path 

from handle_intro.utils.helpers import get_attr
from handle_intro.infra.script import Script

from handle_intro.models.page import Section
from handle_intro.models.saved_file import SavedFile
from handle_intro.models.video import MyVideo 

from handle_intro.utils.helpers import generate_id
from handle_intro.utils.video import get_video_duration

from handle_intro.models.intro import Intro

SCRIPT_NAME = "HANDLE INTROS"
NO_DATA  = "No Sections" 
ERROR_SCRIPT = "Could not handle intros"

class HandleIntro(Script):
   
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

        self.intro_text = get_attr(self.config, 'intro_text', '')

        self.text_robot = text_robot

        

    
   


       
    






    












    
    

         
