from src.controllers.interfaces.legal_person_creator_controller import LegalPersonCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalPersonCreatorView(ViewInterface):
    def __init__(self, controller: LegalPersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_person_info = http_request.body
        body_response = self.__controller.create(legal_person_info)

        return HttpResponse(status_code=201, body=body_response)