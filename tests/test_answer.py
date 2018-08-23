from app.models.answer import Answer
from app.models.question import Question
import pytest
from werkzeug.exceptions import HTTPException


@pytest.fixture
def answerObject(scope="module"):
    answerObject = Answer()
    yield answerObject


@pytest.fixture
def questionObject(scope="module"):
    questionObject = Question()
    questionObject.questions = [{
        'questionId': 2,
        'title': 'what do you mean',
        'body': 'I have no idea what you mean'
    }]
    yield questionObject


def test_get_answers(answerObject):
    assert len(answerObject.get_answers(2)) == 0
    assert isinstance(answerObject.get_answers(2), list)
    assert answerObject.answerId == None
    assert answerObject.questionId == 2


def test_add_answer(answerObject, questionObject):
    answerObject.questionId = 2
    answerObject.answer_body = 'It means you mean something'
    assert len(questionObject.fetch_single_question(
        answerObject.questionId)) == 3
    assert questionObject.fetch_single_question(
        answerObject.questionId)
    with pytest.raises(HTTPException):
        assert isinstance(answerObject.add_answer(
            answerObject.questionId, answerObject.answer_body), dict)
