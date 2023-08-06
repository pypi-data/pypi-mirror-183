from handle_credits.services.base_service import BaseService
from handle_credits.models.request import Request


class BaseController:

    def __init__(self, request: Request, service: BaseService):
        
        self.request = request
        self.service = service

        
    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    