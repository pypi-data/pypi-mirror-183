from add_disclaimers.controllers.base_controller import BaseController
from add_disclaimers.services.base_service import BaseService

from add_disclaimers.models.request import Request

from add_disclaimers.factories.base_factory import BaseFactory

#Infra
#download
from file_transfer.infra.s3_downloader.s3_downloader import S3Downloader 
from file_transfer.infra.local_downloader.local_downloader import LocalDownloader 
from file_saver.infra.mongo_downloader.mongo_downloader import MongoDownloader


from add_disclaimers.infra.add_disclaimers.add_disclaimers import AddDisclaimers

#Services
from add_disclaimers.services.add_disclaimers_service import AddDisclaimersService

#Controllers
from add_disclaimers.controllers.add_disclaimers_controller import  AddDisclaimersController




from add_disclaimers.utils.helpers import *


class Factory(BaseFactory):
   
  
    def __init__(self, request: Request, logger = None):
        super().__init__(request, logger)                                      


    def make_script(self, script_name, general_config, script_config):
        downloader = self.make_downloader(script_name, general_config, script_config)
        return AddDisclaimers(script_config, downloader = downloader, logger = self.logger)

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
        
        executer = self.make_script(script_name, general_config, script_config)
       
        return AddDisclaimersService(script_config, executer)

    def make_controller(self) -> BaseController:
        
        route = self.request.route
        script_name = self.get_script_name(route)
        service = self.make_service(script_name, self.general_config, self.script_config)
        
        controller = AddDisclaimersController(self.request, service)

        return controller     



        

    
    