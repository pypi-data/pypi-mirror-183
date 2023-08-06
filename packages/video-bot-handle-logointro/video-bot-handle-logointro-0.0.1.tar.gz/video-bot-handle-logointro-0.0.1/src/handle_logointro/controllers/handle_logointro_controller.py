from handle_logointro.services.base_service import BaseService

from handle_logointro.models.request import Request
from handle_logointro.controllers.base_controller import BaseController


class HandleLogoIntroController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    