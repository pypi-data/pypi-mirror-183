from handle_credits.services.base_service import BaseService

from handle_credits.models.request import Request
from handle_credits.controllers.base_controller import BaseController


class HandleCreditsController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    