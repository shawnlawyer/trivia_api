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
                    "question" : values.get('question',''),
                    "answer" : values.get('answer',''),
                    "category_id" : values.get('category', ''),
                    "difficulty" : values.get('difficulty', '')
                }

            model = Question(**kwargs)

            db.session.add(model)
            db.session.commit()

            response = {
                "success" : True,
                "question" : model.format()
            }

        except:

            abort(422)

        return jsonify(response)


    @staticmethod
    def edit_action(id, kwargs=None):
        """Edit a Question record

        :param id: record id
        :param kwargs: dictionary to override request form values
        :type id: int
        :type kwargs: dict

        """

        try:

            if not kwargs:

                 kwargs = {
                    "question" : request.form.get('question',''),
                    "answer" : request.form.get('answer',''),
                    "category" : request.form.get('category',''),
                    "difficulty" : request.form.get('difficulty','')
                }

            model = Question.query.filter(Question.id == id).update(kwargs)

            db.session.commit()

            response = {
                "success" : True,
                "data" : model.format()
            }

        except:

            abort(422)

        return jsonify(response)


    @staticmethod
    def delete_action(id):
        """Delete a Question record

        :param id: record id
        :type id: int

        """

        try:

            model = Question.query.filter(Question.id == id).one_or_none()

            db.session.delete(model)
            db.session.commit()

            response = {
                "success" : True
            }

        except:

            abort(422)

        return jsonify(response)


    @staticmethod
    def list_json(page=None):
        """Returns json of a list of Question records

        :param page: page number
        :type page: int

        """

        if not page:

            page = request.args.get('page', 1, type=int)

        models = Question.query.paginate(page=page, per_page=QUESTIONS_PER_PAGE)

        results = {
            "questions": [model.format() for model in models.items],
            "total_questions": Question.query.count(),
            "categories": [model.format() for model in Category.query.all()],
            "current_category": Category.query.first().type
        }
        return jsonify(results)


    @staticmethod
    def search_json(payload={}):
        """Returns json of a list of Question search records

        :param search: search text
        :param page: page number
        :type search: str
        :type page: int

        """

        if not payload:

            payload = request.get_json()

        search = payload.get('searchTerm', '')

        page = payload.get('page', 1)

        count = Question.query.filter(Question.question.ilike("%" + search + "%")).count()
        models = Question.query.filter(Question.question.ilike("%" + search + "%"))\
            .paginate(page=page, per_page=QUESTIONS_PER_PAGE)

        results = {
            "questions": [model.format() for model in models.items],
            "total_questions": count
        }

        return jsonify(results)
