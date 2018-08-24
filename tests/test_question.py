from app.models.question import Question
import pytest
from werkzeug.exceptions import HTTPException


@pytest.fixture
def questionObject(scope="module"):
    questionObject = Question()
    yield questionObject


def test_fetch_all_questions(questionObject):
    assert len(questionObject.fetch_all_questions()) == 1


def test_fetch_single_question(questionObject):
#     with pytest.raises(HTTPException):
#         questionObject.fetch_single_question(2)
    questionObject.title = "What is 404 stand for"
    questionObject.body = "What is 404 I dont understand"
    questionObject.add_question(questionObject.title, questionObject.body)
    assert len(questionObject.fetch_single_question(1)) == 3
    assert isinstance(questionObject.fetch_single_question(1), dict)


def test_add_question(questionObject):
    questionObject.title = "What is 404 stand for"
    questionObject.body = "What is 404 I dont understand"
    questionObject.add_question(questionObject.title, questionObject.body)
    assert len(questionObject.fetch_all_questions()) == 1
    assert isinstance(
        questionObject.add_question(questionObject.title, questionObject.body),
        dict
    )
    assert 'error' in questionObject.add_question(
        questionObject.title, questionObject.body)
    questionObject.title = "What is 404"
    questionObject.body = "What is 404 I dont understand"
    assert questionObject.add_question(
        questionObject.title, questionObject.body)['questionId'] == 2
