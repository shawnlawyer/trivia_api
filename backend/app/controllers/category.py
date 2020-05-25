from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, abort

from app import db
from app.models import Category, Question

QUESTIONS_PER_PAGE=10

class controller(object):

    @staticmethod
    def list_json():
        """Returns a json list of Category types"""

        models = Category.query.all()

        return jsonify([model.format() for model in models])

    @staticmethod
    def list_questions_json(category_id, page=None):
        """Returns json of a list of Question records

        :param category_id: category id
        :param page: page number
        :type page: int

        """
        if not page:

            page = request.args.get('page', 1, type=int)

        count = Question.query.filter(Question.category_id == category_id).count()

        models = Question.query.filter(Question.category_id == category_id)\
            .paginate(page=page, per_page=QUESTIONS_PER_PAGE)

        if not models.items:

            abort(404)

        results = {
            "questions": [model.format() for model in models.items],
            "total_questions": count
        }

        return jsonify(results)

