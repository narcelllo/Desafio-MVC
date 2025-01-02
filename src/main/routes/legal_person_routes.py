from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.legal_person_creator_composer import legal_person_creator_composer
from src.main.composer.legal_person_finder_composer import legal_person_finder_composer

legal_person_rout_bp = Blueprint("legal_person_rout", __name__)

@legal_person_rout_bp.route("/legal_person", methods=["POST"])
def create_person():
    http_request = HttpRequest(body=request.json)
    view = legal_person_creator_composer()
    http_response = view.handle(http_request)
    
    return jsonify(http_response.body), http_response.status_code

@legal_person_rout_bp.route("/legal_person/<legal_person_id>", methods=["GET"])
def finder_person(legal_person_id):
    http_request = HttpRequest(param={"id":legal_person_id})
    view = legal_person_finder_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
