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
    questionObject.title = "What is 404 stand for"
    questionObject.body = "What is 404 I dont understand"
    qObject = questionObject.add_question(questionObject.title, questionObject.body)
    yield qObject


@pytest.fixture
def questionObj(scope="module"):
    questionObject = Question()
    
    yield questionObject


def test_get_answers(answerObject):
    assert len(answerObject.get_answers(2)) == 0
    assert isinstance(answerObject.get_answers(2), list)
    assert answerObject.answerId == None
    assert answerObject.questionId == 2


def test_add_answer(answerObject, questionObject, questionObj):
    questionObj.title = "What is 404 stand for"
    questionObj.body = "What is 404 I dont understand"
    answerObject.questionId = 1
    answerObject.answer_body = 'It means you mean something'
    answerObject.add_answer(answerObject.questionId, answerObject.answer_body)
    qresult = questionObj.fetch_single_question(
        answerObject.questionId)
    assert len(qresult) == 3
    assert isinstance(qresult, dict)
    # with pytest.raises(HTTPException):
    #     assert isinstance(answerObject.add_answer(
    #         answerObject.questionId, answerObject.answer_body), dict)
