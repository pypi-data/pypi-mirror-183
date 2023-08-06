from add_disclaimers.utils.helpers import generate_id, get_attr
from add_disclaimers.infra.script import Script
from add_disclaimers.models.disclaimer import Disclaimer

from add_disclaimers.utils.text  import read_from_file
from add_disclaimers.utils.file  import get_extension
from add_disclaimers.utils.markdown import read_from_md
from add_disclaimers.utils.html import unescape_text


SCRIPT_NAME = "ADD DISCLAIMERS"
NO_DATA  = "No Sections" 
ERROR_SCRIPT = "Could not add disclaimers"

NOT_IMPLEMENTED='Source type is not implemented'


class AddDisclaimers(Script):
   
    def __init__(self, config, downloader = None, logger = None):
        
        super().__init__(SCRIPT_NAME, logger)

        self.config = config
        self.downloader = downloader

        self.on_lambda = get_attr(self.config, 'on_lambda', False)
        self.data = get_attr(self.config, 'data', {})
        self.temp_directory = get_attr(self.config, 'temp_directory', '/tmp')
        self.channel_info = get_attr(self.config, "channel_info", {})
        self.disclaimers = get_attr(self.config, 'disclaimers', [])


      
    def __replace_placeholders(self, text):
        
        channel_info = self.channel_info
        new_text = text

        show_business_contact = get_attr(channel_info, 'show_business_contact', '')
        business_contact = get_attr(channel_info, 'business_email', '')
        if (show_business_contact == False):
            business_contact = ''

        new_text = str(new_text).replace("{{business_contact}}", f"{business_contact}") 
        channel_name = get_attr(channel_info, 'name', '')
        new_text = str(new_text).replace("{{channel_name}}", f"{channel_name}")  

        return new_text  

    
    def read_text_from_file(self, file):
        
        extension = get_extension(file)
        if (extension == 'md'):
            text = read_from_md(file)
        elif (extension == 'txt'):
            text = read_from_file(file)
        else:    
            text = read_from_file(file)

        
        return text

    def set_downloader(self, downloader):
        self.downloader =  downloader

    def create_disclaimer(self, disclaimer):

        source_type = get_attr(disclaimer, 'source_type', 'text')
        text = ''

        #if disclaimer is on md remote file, do the download
        if (source_type == 's3'):
            source_info = get_attr(disclaimer, 'source_info', {})
            downloaded_files = self.download_source_file(source_info)
            text = self.read_text_from_file(downloaded_files[0])
            text = self.__replace_placeholders(text)
        elif (source_type == 'text'):
            text = get_attr(disclaimer, 'text', '')
            text = self.__replace_placeholders(text)
        else:
            raise Exception(NOT_IMPLEMENTED)

        disclaimer_title = get_attr(disclaimer, 'disclaimer_title', '')
        disclaimer_type = get_attr(disclaimer, 'disclaimer_type', '')
        time_on_screen = get_attr(disclaimer, 'time_on_screen', '')
        unescaped_text = unescape_text(text)

        disclaimer_object =  Disclaimer(
                                id = generate_id(),
                                title = disclaimer_title, 
                                type = disclaimer_type, 
                                text = text, 
                                time = time_on_screen, 
                                unescaped_text = unescaped_text)

        return disclaimer_object                        


    def download_source_file(self, source_info):
        
        downloaded_files = []
        download_results = []
        saved_files = []

        source_bucket = get_attr(source_info,'source_bucket', '' )
        source = get_attr(source_info,'source', {} )
        directory = get_attr(source,'directory', '')
        objects = get_attr(source,'objects', [])
        file = objects[0]

        download_source = {'source_bucket' : source_bucket, "sources": [{ "directory": directory, "objects": [file] }]}
        self.downloader.reset_sources()
        self.downloader.add_sources(download_source)

        download_results, downloaded_files = self.downloader.run()
        return downloaded_files

   


       
    






    












    
    

         
