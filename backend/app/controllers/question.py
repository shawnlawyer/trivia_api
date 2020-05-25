from flask import render_template, request, flash, redirect, url_for, jsonify, abort

from app import db
from app.models import Question, Category


QUESTIONS_PER_PAGE = 10

class controller(object):


    @staticmethod
    def create_action(kwargs=None):
        """Creates a Question record

        :param kwargs: dictionary to override request form values
        :type kwargs: dict

        """

        try:

            if not kwargs:

                values = request.get_json()

                kwargs = {
                    "question" : values.get('question'),
                    "answer" : values.get('answer'),
                    "category_id" : int(values.get('category', 0)),
                    "difficulty" : int(values.get('difficulty', 0))
                }

            model = Question(**kwargs)

            model.insert()

            response = {
                "success" : True,
                "question" : model.format()
            }

            return jsonify(response)

        except:

            abort(422)

    @staticmethod
    def delete_action(id):
        """Delete a Question record

        :param id: record id
        :type id: int

        """

        model = Question.query.filter(Question.id == id).first_or_404()

        model.delete()

        response = {
            "success" : True
        }

        return jsonify(response)

    @staticmethod
    def list_json(page=None):
        """Returns json of a list of Question records

        :param page: page number
        :type page: int

        """

        try:

            if not page:

                page = request.args.get('page', 1, type=int)

            models = Question.query.paginate(page=page, per_page=QUESTIONS_PER_PAGE)

            if not models.items:

                abort(404)

            results = {
                "questions": [model.format() for model in models.items],
                "total_questions": Question.query.count(),
                "categories": [model.format() for model in Category.query.all()],
                "current_category": "ALL"
            }

            return jsonify(results)

        except:

            abort(422)

    @staticmethod
    def search_json(payload={}):
        """Returns json of a list of Question search records

        :param payload: payload dict
        :param page: page number
        :type search: str
        :type page: int

        """

        if not payload:

            payload = request.get_json()
            page = payload.get('page', request.args.get('page', 1))

        search = payload.get('searchTerm', '')

        query = Question.query.filter(Question.question.ilike("%" + search + "%"))

        count = query.count()

        models = query.paginate(page=page, per_page=QUESTIONS_PER_PAGE)

        if not models.items:

            abort(404)

        results = {
            "questions": [model.format() for model in models.items],
            "total_questions": count
        }

        return jsonify(results)

