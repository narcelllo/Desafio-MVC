from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.legal_person_routes import legal_person_rout_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(legal_person_rout_bp)