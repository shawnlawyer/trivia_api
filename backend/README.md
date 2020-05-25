# Full Stack Trivia API Backend



### Tech Stack

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


### Development Setup
```

cp .env.example .env   
  
docker-compose up -d --build  
  
docker exec -it trivia_api_app_1 bash

cd backend

python3 migrate.py db upgrade

```

browse to http://localhost/

## Testing

```

docker exec -it trivia_api_app_1 bash

cd backend

python3 test.py

```

##API Documentation

#### GET '/categories'

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An array of objects, id :category_id and type: category_string. 
```
[
  {
    "id": 1, 
    "type": "Science"
  }, 
  {
    "id": 2, 
    "type": "Art"
  }, 
  {
    "id": 3, 
    "type": "Geography"
  }, 
  {
    "id": 4, 
    "type": "History"
  }, 
  {
    "id": 5, 
    "type": "Entertainment"
  }, 
  {
    "id": 6, 
    "type": "Sports"
  }
]

```

#### GET /api/questions?page=<page_number>

- Fetches a dictionary of questions in which the keys are the answer, category, difficulty, id and question.
- Request Arguments: page
- Returns: An object with keys categories, current_category, questions, and total_questions.

Example Response

```
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "current_category": "Science", 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": "History", 
      "category_id": 4, 
      "difficulty": 2, 
      "id": 1, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "History", 
      "category_id": 4, 
      "difficulty": 1, 
      "id": 2, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": "Entertainment", 
      "category_id": 5, 
      "difficulty": 4, 
      "id": 3, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "Entertainment", 
      "category_id": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "Entertainment", 
      "category_id": 5, 
      "difficulty": 3, 
      "id": 5, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": "Sports", 
      "category_id": 6, 
      "difficulty": 3, 
      "id": 6, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "Sports", 
      "category_id": 6, 
      "difficulty": 4, 
      "id": 7, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "History", 
      "category_id": 4, 
      "difficulty": 2, 
      "id": 8, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "Geography", 
      "category_id": 3, 
      "difficulty": 2, 
      "id": 9, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "Geography", 
      "category_id": 3, 
      "difficulty": 3, 
      "id": 10, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "total_questions": 19
}
```

#### DELETE /api/questions/<question_id>

Delete question

- Request Arguments: Question Id
- Returns: An object with key success: true.

Example Response

```
{
    "success":true
}
```

#### POST /api/questions

Create question

- Request Body: question, answer, difficulty and category.
- Returns: An object with keys success and question.

Example Request Payload

```
{
    "answer": "Muhammad Ali",
    "category": 4, 
    "difficulty": 1, 
    "question": "What boxer's original name is Cassius Clay?"
}
```

Example Response

```
{
  "question":{
      "answer": "Muhammad Ali", 
      "category": "History", 
      "category_id": 4, 
      "difficulty": 1, 
      "id": 2, 
      "question": "What boxer's original name is Cassius Clay?"
  },
  "success": true
}
```

#### POST /api/questions/search

Retrieve questions based on search 

- Request Arguments: Page Number
- Request Body: An object with key searchTerm
- Returns: An object with keys questions, total_questions.

Example Request Payload

```
{
    "searchTerm": "what"
}
```

Example Response

```
{
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": "History", 
      "category_id": 4, 
      "difficulty": 1, 
      "id": 2, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": "Entertainment", 
      "category_id": 5, 
      "difficulty": 4, 
      "id": 3, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "Entertainment", 
      "category_id": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "Entertainment", 
      "category_id": 5, 
      "difficulty": 3, 
      "id": 5, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "Geography", 
      "category_id": 3, 
      "difficulty": 2, 
      "id": 9, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "Art", 
      "category_id": 2, 
      "difficulty": 3, 
      "id": 13, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "The Liver", 
      "category": "Science", 
      "category_id": 1, 
      "difficulty": 4, 
      "id": 16, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Blood", 
      "category": "Science", 
      "category_id": 1, 
      "difficulty": 4, 
      "id": 18, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "total_questions": 8
}
```

#### POST /api/categories/<int:category_id>/questions

Retrieve questions based on category

- Request Arguments: An object with keys category_id, page.
- Returns: An object with keys categories, current_category, questions, and total_questions


Example Response 

```
{
  "questions": [
    {
      "answer": "Escher", 
      "category": "Art", 
      "category_id": 2, 
      "difficulty": 1, 
      "id": 12, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "Art", 
      "category_id": 2, 
      "difficulty": 3, 
      "id": 13, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "Art", 
      "category_id": 2, 
      "difficulty": 4, 
      "id": 14, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": "Art", 
      "category_id": 2, 
      "difficulty": 2, 
      "id": 15, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "total_questions": 4
}
```

#### POST /api/quizzes

Retrieve questions to play the quiz.

- Request Body: An object with keys quiz_category and previous_questions.
- Returns: An object with keys question, answer, category_id, category, and difficulty

Example Request Payload

```
{
    previous_questions: [],
    quiz_category: {
        type: "Art",
        id: 2
    }
}
```

Example Response 

```
{
  "answer": "One", 
  "category": "Art", 
  "category_id": 2, 
  "difficulty": 4, 
  "id": 14, 
  "question": "How many paintings did Van Gogh sell in his lifetime?"
}
```

