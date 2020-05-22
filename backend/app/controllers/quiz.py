from flask import render_template, request, flash, redirect, url_for, jsonify, abort
import math, random
from app import db
from app.models import Question, Category


QUESTIONS_PER_PAGE = 10

class controller(object):

    @staticmethod
    def quiz_json(payload={}):
        """Returns json of a list of Question search records

        :param payload: { "previous_questions:"[1,2,5,7], "category": `id` eg. 5 }
        :type payload: dict

        """

        if not payload:

            payload = request.get_json()

        category_id = payload.get('quiz_category', {}).get('id', 0)

        category = Category.query.filter(Category.id == category_id).one_or_none()

        if category:

            count = Question.query\
                .filter(~Question.id.in_(payload.get('previous_questions',[])), Question.category_id == category.id)\
                .count()

        else:

            count = Question.query.filter(~Question.id.in_(payload.get('previous_questions',[]))).count()

        offset = math.floor( random.random() * count )

        if category:

            question = Question.query\
                .filter(~Question.id.in_(payload.get('previous_questions',[])), Question.category_id == category.id)\
                .offset(offset).limit(1).one_or_none()

        else:

            question = Question.query\
                .filter(~Question.id.in_(payload.get('previous_questions',[]))).offset(offset).limit(1).one_or_none()

        try:

            result = question.format()

        except:

            result = {}

        return jsonify(result)
