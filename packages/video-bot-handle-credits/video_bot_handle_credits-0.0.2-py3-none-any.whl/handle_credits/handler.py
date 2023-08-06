from logger import Logger
from handle_credits.utils.lambda_helpers  import * 
from handle_credits.models.request import Request
from handle_credits.factories.factory import Factory

def handler(event, context):

    request = Request(event)
    logger = Logger()
    factory = Factory(request, logger)
    controller = factory.make_controller()
    result = controller.handle()

    json_str = get_json(result)
    
    print(json_str)
    
    return json_str