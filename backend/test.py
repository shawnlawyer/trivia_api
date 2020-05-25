import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app, db
from app.models import Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.db = db
    
    def tearDown(self):
        """Executed after tests"""
        pass

    def test_get_categories(self):

        response = self.client().get("/api/categories")

        data = json.loads(response.data.decode())

        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), Category.query.count())

    def test_get_categories_post_method_405_error(self):

        response = self.client().post("/api/categories")

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 405)
        self.assertFalse(data.get("success", True))

    def test_get_questions(self):

        response = self.client().get("/api/questions")

        data = json.loads(response.data.decode())

        self.assertTrue(isinstance(data.get("questions"), list))
        self.assertEqual(data.get("total_questions"), Question.query.count())

    def test_get_questions_post_method_405_error(self):

        response = self.client().post("/api/questions")

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 405)
        self.assertFalse(data.get("success", True))

    def test_delete_question(self):

        kwargs = {
            "question": "Test Question",
            "answer": "Test Answer",
            "category_id": 1,
            "difficulty": 1,
        }

        question = Question(**kwargs)

        question.insert()

        response = self.client().delete("/api/questions/{}".format(question.id))

        question = Question.query.filter(Question.question == kwargs.get('question')).one_or_none()

        self.assertIsNone(question)

    def test_delete_question_not_found_404_error(self):

        response = self.client().delete("/api/questions/{}".format(0))

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data.get("success", True))

    def test_create_question(self):

        kwargs = {
            "question": "Test Question",
            "answer": "Test Answer",
            "category": 1,
            "difficulty": 1,
        }

        response = self.client().post(
            "/api/questions/create",
            json=kwargs
        )

        data = json.loads(response.data.decode())

        question = Question.query.filter(Question.question == kwargs.get('question')).one_or_none()

        self.assertIsNotNone(question)

        question.delete()

    def test_create_question_unprocessable_422_error(self):

        kwargs = {
            "question": False,
            "answer": False,
            "category": "test",
            "difficulty": "test",
        }

        response = self.client().post(
            "/api/questions/create",
            json=kwargs
        )


        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data.get("success", True))

    def test_search_questions(self):

        response = self.client().post(
            "/api/questions/search",
            json={"searchTerm": "What"}
        )

        data = json.loads(response.data.decode())

        self.assertTrue(isinstance(data.get("questions"), list))

    def test_post_search_questions(self):

        response = self.client().post(
            "/api/questions/search",
            json={"searchTerm": "What"}
        )

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data.get("questions"), list))

    def test_post_search_questions_not_found_404_error(self):

        response = self.client().post(
            "/api/questions/search",
            json={"searchTerm": "rkwksjkwrkj"}
        )

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data.get("success", True))

    def test_post_question_by_category(self):

        response = self.client().post("/api/categories/1/questions")

        data = json.loads(response.data.decode())

        category = Category.query.filter(Category.id==1).first()

        self.assertTrue(isinstance(data.get("questions"), list))
        self.assertEqual(data.get("total_questions"), len(category.questions))

    def test_post_question_by_category_not_found_404_error(self):

        response = self.client().post("/api/categories/99/questions")

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data.get("success", True))

    def test_post_quizzes(self):

        response = self.client().post(
            "/api/quizzes",
            json={"previous_questions": [], "quiz_category": {"type": "Science", "id": 1}}
        )

        data = json.loads(response.data.decode())

        self.assertEqual(data.get("category_id"), 1)
        self.assertEqual(data.get("category"), "Science")

    def test_404_error(self):

        response = self.client().get("/api/not_an_endpoint")

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data.get("success", True))

    def test_405_error(self):

        response = self.client().post("/api/categories")

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 405)
        self.assertFalse(data.get("success", True))

    def test_422_error(self):

        kwargs = {
            "test": ""
        }

        response = self.client().post(
            "/api/questions/create",
            json=kwargs
        )

        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 422)
        self.assertFalse(data.get("success", True))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
