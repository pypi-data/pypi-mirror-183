from handle_credits.services.base_service import BaseService
from handle_credits.utils.helpers import get_attr
from handle_credits.utils.service_helper import map_service_config

class SpeechService(BaseService):

    def __init__(self, config, executer):

        self.config = config
        self.executer = executer
        self.temp_directory =  get_attr(self.config,  'temp_directory', '/tmp')
       
    def get_speech_for_sentence(self, sentence):
        dict_sentence = sentence.__dict__
        payload = map_service_config(self.config,  "sentence", dict_sentence)
        result = self.executer.execute(payload = payload, service_path = '/sentence')
        return result['speech']