from add_disclaimers.services.base_service import BaseService

from add_disclaimers.models.request import Request
from add_disclaimers.controllers.base_controller import BaseController


class AddDisclaimersController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    