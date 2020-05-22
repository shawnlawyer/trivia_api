from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.controllers import QuizController

blueprint = Blueprint('quiz', __name__)
controller = QuizController()

@blueprint.route('/quizzes', methods=['POST'])
def quiz_json():

    return controller.quiz_json()

