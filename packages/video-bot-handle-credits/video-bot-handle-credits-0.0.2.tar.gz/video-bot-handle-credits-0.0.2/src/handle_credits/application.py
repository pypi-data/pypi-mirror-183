from dotenv import load_dotenv

from handle_credits.handler import handler
from handle_credits.utils.lambda_helpers import get_json
from handle_credits.get_event import get_event



class Application:
   
    def run(self):
        load_dotenv()
        event = get_event()
        result = handler(event, None)
        json_str = get_json(result)
        return json_str
           


    

  








    

    
    
