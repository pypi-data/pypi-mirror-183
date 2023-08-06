from logger import Logger
from add_disclaimers.utils.lambda_helpers  import * 
from add_disclaimers.models.request import Request
from add_disclaimers.factories.factory import Factory

def handler(event, context):

    request = Request(event)
    logger = Logger()
    factory = Factory(request, logger)
    controller = factory.make_controller()
    result = controller.handle()

    json_str = get_json(result)
    
    print(json_str)
    
    return json_str