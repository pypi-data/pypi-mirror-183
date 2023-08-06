from add_disclaimers.services.base_service import BaseService
from add_disclaimers.utils.helpers import get_attr


class AddDisclaimersService(BaseService):

    
    def __init__(self, config, executer):

        self.config = config

        self.channel_info = get_attr(self.config, "channel_info", {})

        self.disclaimers = get_attr(self.config,  'disclaimers', [])

        if (len(self.disclaimers) == 0):
            raise Exception('Disclaimers must be informed")')

  
        #workers
        self.executer = executer
        self.temp_directory =   get_attr(self.config,  'temp_directory', '/tmp')
   

    def execute(self):
       
        disclaimers = self.disclaimers
        resulted_disclaimers = []   
        disclaimer_object = None  
        
        for disclaimer in disclaimers:
            disclaimer_object = self.executer.create_disclaimer(disclaimer)
            resulted_disclaimers.append(disclaimer_object)
        
        return resulted_disclaimers
