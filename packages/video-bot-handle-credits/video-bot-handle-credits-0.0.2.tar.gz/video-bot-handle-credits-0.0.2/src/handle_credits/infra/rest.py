from handle_credits.utils.helpers import get_attr
from handle_credits.infra.script import Script

from handle_credits.infra.aws_request import AWSRequest
import requests 
import json



SCRIPT_NAME="REST"




class Rest(Script):
   
    def __init__(self, config, logger = None):
        
        super().__init__(SCRIPT_NAME, logger)

        self.config = config
        
        self.on_lambda = get_attr(self.config, 'on_lambda', False)
        self.data = get_attr(self.config, 'data', {})
        self.temp_directory = get_attr(self.config, 'temp_directory', '/tmp')

        self.connection = get_attr(self.config, 'connection', {})

        self.base_url = get_attr(self.connection, 'base_url', '')
        self.method = get_attr(self.connection, 'method', 'POST')
        self.authentication = get_attr(self.connection, 'authentication', {})
        self.authentication_type = get_attr(self.authentication, 'type', '')

        
    def __get_headers(self):
        return self.authentication

    
    def execute(self, payload, service_path):

        result = {}

        #removes the path / in the end and in the begining  
        if(str(service_path).startswith('/')):
            service_path = service_path[1:len(service_path)]

        if(str(service_path).endswith('/')):
            service_path = service_path[0:len(service_path)-1]
        
        endpoint = self.base_url + '/' + service_path

        if (self.authentication_type == 'awsv4'):

            aws_requester = AWSRequest({ **self.authentication, "endpoint" : endpoint })
            json_payload = json.dumps(payload)
            response = aws_requester.request(endpoint = endpoint, payload = json_payload )
            if (response.ok == True):
                result = response.json()
            else:
                raise Exception(response.content)

            

        else:

            headers = self.__get_headers()

            if (self.method == 'POST'):
                response = requests.post(endpoint, data = payload, headers = headers)
                if (response.ok == True):
                    result = response.json()
                else:
                    raise Exception(response.content)


            if (self.method == 'GET'):
                response = requests.get(endpoint, data = payload, headers = headers)    
                if (response.ok == True):
                    result = response.json()
                else:
                    raise Exception(response.content)


        

        return result
