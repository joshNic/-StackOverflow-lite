from app.mockdbhelper import MockDBHelper
import pytest
import json
from flask import request


@pytest.fixture
def setup_mockdb(scope="module"):
    mockObject = MockDBHelper()
    yield mockObject


def test_fetch_all_questions(setup_mockdb):
    assert len(setup_mockdb.fetch_all_questions()) == 1
    assert len(setup_mockdb.fetch_all_questions()['questions']) == 0


def test_fetch_single_question(setup_mockdb, client):
    # assert not isinstance(setup_mockdb.fetch_single_question(2), dict)
    # assert len(setup_mockdb.fetch_single_question(2)) == 2
    # assert setup_mockdb.fetch_single_question(2)['question']['questionId']==2
    with pytest.raises(Exception):
        setup_mockdb.fetch_single_question(3)


def test_add_question(make_response_post_question, setup_mockdb):
    assert make_response_post_question.json != setup_mockdb.add_question()
    assert isinstance(setup_mockdb.add_question(), dict)
    # assert setup_mockdb.add_question() != {'question': QUESTIONS}
    assert len(setup_mockdb.add_question()) == 1
    with pytest.raises(Exception):
        setup_mockdb.add_question(2)


def test_add_answer(make_response_post_answer, setup_mockdb):
    with pytest.raises(Exception):
        setup_mockdb.add_answer()
    with pytest.raises(Exception):
        setup_mockdb.add_answer(20)
