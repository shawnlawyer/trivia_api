from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.controllers import QuestionController

blueprint = Blueprint('question', __name__)
controller = QuestionController()

@blueprint.route('/questions/create', methods=['POST'])
def create_action():
    '''
    An endpoint to POST a new question.

    :param question: question text
    :param answer: answer text
    :param category: question category
    :param difficulty: difficulty rating
    :type question: str
    :type answer: str
    :type category: int
    :type difficulty: int

    '''

    return controller.create_action()

@blueprint.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_action(question_id):
    '''
    An endpoint to DELETE question using a question ID.

    '''

    return controller.delete_action(question_id)

@blueprint.route('/questions')
def list_json():
    '''
    An endpoint to handle GET requests for questions,
    including pagination (every 10 questions).

    Returns a list of questions, number of total questions,
    current category, categories.
    '''


    return controller.list_json()

@blueprint.route('/questions/search', methods=['POST'])
def search_page():
    '''
    A POST endpoint to get questions based on a search term.

    Returns any questions for whom the search term
    is a substring of the question.
    '''

    return controller.search_json()
