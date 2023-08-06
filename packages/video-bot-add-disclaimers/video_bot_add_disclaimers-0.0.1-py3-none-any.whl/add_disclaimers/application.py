from dotenv import load_dotenv

from add_disclaimers.handler import handler
from add_disclaimers.utils.lambda_helpers import get_json
from add_disclaimers.get_event import get_event



class Application:
   
    def run(self):
        load_dotenv()
        event = get_event()
        result = handler(event, None)
        json_str = get_json(result)
        return json_str
           


    

  








    

    
    
