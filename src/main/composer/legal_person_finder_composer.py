from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_person import LegalPersonRepository
from src.controllers.legal_person_finder_controller import LegalPersonFinderController
from src.views.legal_person_finder import LegalPersonFinderView

def legal_person_finder_composer():
    model = LegalPersonRepository(db_connection_handler)
    controller = LegalPersonFinderController(model)
    view = LegalPersonFinderView(controller)

    return view