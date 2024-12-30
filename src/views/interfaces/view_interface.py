from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequiest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):

    @abstractmethod
    def handler(self, http_request: HttpRequiest) -> HttpResponse:
        pass