from flask import Blueprint

from . import projects_blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(projects_blueprint.bp)




