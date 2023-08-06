from handle_intro.services.base_service import BaseService
from handle_intro.utils.helpers import get_attr, set_attr
from handle_intro.utils.service_helper import map_service_config
from handle_intro.utils.file import to_base64


import base64
class AddTimeService(BaseService):

    def __init__(self, config, executer, downloader = None):

        self.config = config
        self.executer = executer
        self.downloader = downloader
        self.temp_directory =  get_attr(self.config,  'temp_directory', '/tmp')

    def get_time_to_sentence(self, sentence, binary_file = None):

        
        dict_sentence = sentence.__dict__
        
        payload = map_service_config(self.config,  "sentence", dict_sentence)

        #add configuration to downloader
        if (binary_file == None):
            if (self.downloader != None):
                set_attr(payload['script_config']['config'],'downloader', self.downloader )
        else: 
            base64_binary_file = to_base64(binary_file) 
            set_attr(payload['script_config']['config']['sentence']['speech'],'binary_file', base64_binary_file)

        result = self.executer.execute(payload = payload, service_path = '/sentence')
        

        return result 
        