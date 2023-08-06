from abc import ABC
from handle_logointro.controllers.base_controller import BaseController
from handle_logointro.services.base_service import BaseService

from handle_logointro.models.request import Request
from handle_logointro.utils.helpers import *
import os

class BaseFactory(ABC):
   

    def get_from_body(self, payload, name):
        try:
            return payload[name]    
        except KeyError as err:
            raise Exception(f'Information required on body: {err}')
        except Exception as general_error:
            raise Exception(general_error) 

    def get_script_name(self, route):
        return route[1:]
  

    def __init__(self, request: Request, logger = None):

        self.request = request
        self.logger = logger

        body = self.request.body

        self.general_config = self.get_from_body(body, 'config')
        self.script_config = self.get_from_body(body, 'script_config')

        self.config_from_environment = self.get_config_from_environment()


    def get_config_from_environment(self):
       
        config = {
                'provider_config' : {
                    'client_id' : os.environ.get('PROVIDER_CLIENT_ID'),
                    'client_secret' : os.environ.get('PROVIDER_CLIENT_SECRET'),
                    'region' : os.environ.get('PROVIDER_REGION')
                }
        }

        return config
        


    def make_infra(self, script_name, general_config, script_config):
        pass

    def make_service(self, script_name, general_config, script_config) -> BaseService:
        pass

    def make_controller(self) -> BaseController:
        pass

  



        

    
    