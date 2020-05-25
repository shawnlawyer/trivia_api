from flask import Blueprint

from app.controllers import CategoryController

blueprint = Blueprint('category', __name__)
controller = CategoryController()

@blueprint.route('/categories')
def list_json():

    return controller.list_json()

@blueprint.route('/categories/<int:category_id>/questions', methods=['post'])
def list_questions_json(category_id):
    '''
    An endpoint retrieve a JSON list of a categories questions.

    '''

    return controller.list_questions_json(category_id)

