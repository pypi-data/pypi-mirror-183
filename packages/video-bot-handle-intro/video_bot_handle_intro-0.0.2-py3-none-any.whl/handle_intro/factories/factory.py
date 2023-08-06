from handle_intro.controllers.base_controller import BaseController
from handle_intro.services.base_service import BaseService

from handle_intro.models.request import Request

from handle_intro.factories.base_factory import BaseFactory

#Infra
#upload
from file_transfer.infra.s3_file_saver.s3_file_saver import S3FileSaver 
from file_transfer.infra.pure_file_saver.pure_file_saver import PureFileSaver 
from file_transfer.infra.local_file_saver.local_file_saver import LocalFileSaver 
from file_saver.infra.mongo_uploader.mongo_uploader import MongoUploader

#download
from file_transfer.infra.s3_downloader.s3_downloader import S3Downloader 
from file_transfer.infra.local_downloader.local_downloader import LocalDownloader 
from file_saver.infra.mongo_downloader.mongo_downloader import MongoDownloader


#rest
from handle_intro.infra.rest  import Rest



from handle_intro.infra.handle_intro.handle_intro import HandleIntro 

#Services
from handle_intro.services.handle_intro_service import HandleIntroService

#Controllers
from handle_intro.controllers.handle_intro_controller import  HandleIntroController

#Other Services
from handle_intro.services.text_utils_service import TextUtilsService
from handle_intro.services.speech_service import SpeechService
from handle_intro.services.time_service import AddTimeService

#from add_time.services.add_time_service import AddTimeService
#from add_time.infra.add_time import AddTime


from handle_intro.utils.helpers import *


class Factory(BaseFactory):
   
  
    def __init__(self, request: Request, logger = None):
        super().__init__(request, logger)                                      


    def make_script(self, script_name, general_config, script_config):
        return HandleIntro(script_config, self.logger)

    def make_external_service(self, script_name, general_config, script_config):
        
        service_config = {}
        services_config = get_attr(script_config, 'services', [])
        
        if (len(services_config)==0):
            raise Exception('Services config key is required')

        if (script_name == 'SPEECH-SERVICE'):
            
            service_config = list(filter(lambda service: service['type'] == 'speech',services_config))
            if (len(services_config) == 0):
                raise Exception('configuration for service speech is required')
            else:
                service_config = service_config[0]['config'] 
                script_config = { **script_config, **service_config }
                rest_executer = Rest(service_config, self.logger)
                return SpeechService(service_config, rest_executer)      

        elif (script_name == 'ADD-TIME-SERVICE'):    

            service_config = list(filter(lambda service: service['type'] == 'add-time',services_config))
            if (len(services_config) == 0):
                raise Exception('configuration for service add-time is required')
            else:
                service_config = service_config[0]['config']
                script_config = { **script_config, **service_config }
                #executer = AddTime(service_config, self.logger)
                executer = Rest(service_config, self.logger)
                downloader = script_config['downloader'] 
                #return AddTimeService(service_config, executer) 
                return AddTimeService(service_config, executer, downloader) 

        elif (script_name == 'TEXT-UTILS-SERVICE'):   

            service_config = list(filter(lambda service: service['type'] == 'text-utils',services_config))
            if (len(services_config) == 0):
                raise Exception('configuration for service text-utils is required')
            else:
                service_config = service_config[0]['config']  
                script_config = { **script_config, **service_config }
                rest_executer = Rest(service_config, self.logger)
                return TextUtilsService(service_config, rest_executer)

        else:
            raise Exception('Script name is not valid: ' + script_name)

        

        
    def make_saver(self, script_name, general_config, script_config):
        if (script_name == ''):
            if ('saver' not in script_config):
                raise Exception('saver configuration key is required')

            saver_type = script_config['saver']['type']

            script_config['saver'] = { **script_config['saver'], 'temp_directory': get_attr(script_config,'temp_directory','/tmp') }

            if (saver_type == 's3'):
                return S3FileSaver(script_config['saver'])   
            if (saver_type == 'local'):
                return LocalFileSaver(script_config['saver'])      
            elif (saver_type == 'download'):
                script_config['compress'] = True
                return PureFileSaver(script_config['saver'])    
            elif (saver_type == 'mongo'):
                return MongoUploader(script_config['saver'])              
            else:    
                raise Exception(f'Saver type not implemented: {saver_type}')    



    def make_downloader(self, script_name, general_config, script_config):
        

            if ('downloader' not in script_config):
                raise Exception('downloader configuration key is required')

            downloader_type = script_config['downloader']['type']

            script_config['downloader'] = { **script_config['downloader'], 'temp_directory': get_attr(script_config,'temp_directory','/tmp') }

            if (downloader_type == 's3'):
                return S3Downloader(script_config['downloader'])
            elif (downloader_type == 'local'):
                return LocalDownloader(script_config['downloader'])    
            elif (downloader_type == 'mongo'):
                return MongoDownloader(script_config['downloader'])      
            else:
                raise Exception(f'Downloader type not implemented: {downloader_type}')    

  
    def make_service(self, script_name, general_config, script_config) -> BaseService:
        
        script_config = script_config['config']

        saver = self.make_saver(script_name, general_config, script_config)
        downloader = self.make_downloader(script_name, general_config, script_config)
        executer = self.make_script(script_name, general_config, script_config)

        #adds external services into the main service
        external_services = []
        speech_service = self.make_external_service('SPEECH-SERVICE', general_config, script_config)
        time_service = self.make_external_service('ADD-TIME-SERVICE', general_config, script_config)
        text_service = self.make_external_service('TEXT-UTILS-SERVICE', general_config, script_config)

        external_services.append({'type': 'speech', 'instance': speech_service})
        external_services.append({'type': 'add-time', 'instance': time_service})
        external_services.append({'type': 'text-utils', 'instance': text_service})
       
        return HandleIntroService(script_config, executer, downloader, saver, external_services)

    def make_controller(self) -> BaseController:
        
        route = self.request.route
        script_name = self.get_script_name(route)
        service = self.make_service(script_name, self.general_config, self.script_config)
        
        controller = HandleIntroController(self.request, service)

        return controller     



        

    
    