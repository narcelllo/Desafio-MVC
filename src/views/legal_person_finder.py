from src.controllers.interfaces.legal_person_finder_controller import LegalPersonFinderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalPersonFinderView(ViewInterface):
    def __init__(self, controller: LegalPersonFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_person_id = http_request.param["id"]
        body_response = self.__controller.find(legal_person_id)
        return HttpResponse(status_code=200, body=body_response)