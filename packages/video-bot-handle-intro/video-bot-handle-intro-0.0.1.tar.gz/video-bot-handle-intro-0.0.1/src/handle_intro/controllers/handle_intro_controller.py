from handle_intro.services.base_service import BaseService

from handle_intro.models.request import Request
from handle_intro.controllers.base_controller import BaseController


class HandleIntroController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    