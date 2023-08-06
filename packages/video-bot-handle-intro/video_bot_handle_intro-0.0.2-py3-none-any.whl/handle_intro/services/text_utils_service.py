from handle_intro.services.base_service import BaseService
from handle_intro.utils.helpers import generate_id, get_attr
from  handle_intro.utils.service_helper import map_service_config

class TextUtilsService(BaseService):

    def __init__(self, config, executer):

        self.config = config
        self.executer = executer
        self.temp_directory =  get_attr(self.config,  'temp_directory', '/tmp')

   

    def extract_keywords(self, sentence):
        dict_sentence = sentence.__dict__
        payload = map_service_config(self.config,  "sentence", dict_sentence)
        result = self.executer.execute(payload = payload, service_path = '/extract-keywords-sentence')
        return result['keywords']   

    def generate_subtitles_for_sentence(self, sentence):
        dict_sentence = sentence.__dict__
        payload = map_service_config(self.config,  "sentence", dict_sentence)
        result = self.executer.execute(payload = payload, service_path = '/generate-subtitles-sentence')
        return result['subtitles']  
