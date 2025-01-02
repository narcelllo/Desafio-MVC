from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_person import LegalPersonRepository
from src.controllers.legal_person_creator_controller import LegalPersonCreaterController
from src.views.legal_person_creator_view import LegalPersonCreatorView

def legal_person_creator_composer():
    model = LegalPersonRepository(db_connection_handler)
    controller = LegalPersonCreaterController(model)
    view = LegalPersonCreatorView(controller)

    return view