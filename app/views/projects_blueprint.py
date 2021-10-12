from app.controller.projects_controller import (add_project,
                                             
                                                   show_project_detail,
                                                   delete_project,
                                                   shutdown_session)


from flask import Blueprint


bp = Blueprint('projects_bp', __name__, url_prefix='/projects')


bp.post('/')(add_project)
bp.get('/<project_name>')(show_project_detail)
bp.delete('/<project_name>')(delete_project)
bp.get('/<int:id>')(shutdown_session)
