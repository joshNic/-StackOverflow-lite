import pytest
import json
from flask import request

QUESTIONS = [{
    "questionId": 1,
    "title": "What is does Error 404 mean",
    "body": "So i came across this when i was trying to access my old website"
},
    {
    "questionId": 2,
    "title": "What does Error 400 mean",
    "body": "I have this application which always returns this error please help"
}]


def test_fetch_all_questions(setup_mockdb):
    assert len(setup_mockdb.fetch_all_questions()) == 1
    assert len(setup_mockdb.fetch_all_questions()['questions']) == 2
    assert setup_mockdb.fetch_all_questions(
    )['questions'][0]['title'] == "What is does Error 404 mean"
    assert isinstance(setup_mockdb.fetch_all_questions(), dict)


def test_fetch_single_question(setup_mockdb):
    assert isinstance(setup_mockdb.fetch_single_question(2), dict)
    assert len(setup_mockdb.fetch_single_question(2)) == 1
    assert setup_mockdb.fetch_single_question(2)['question']['questionId'] == 2
    with pytest.raises(Exception):
        setup_mockdb.fetch_single_question(3)


def test_add_question(make_response_post_question, setup_mockdb):
    assert make_response_post_question.json != setup_mockdb.add_question()
    assert isinstance(setup_mockdb.add_question(), dict)
    assert setup_mockdb.add_question() != {'question': QUESTIONS}
    assert len(setup_mockdb.add_question()) == 1
    assert len(setup_mockdb.add_question()['question']) > 2
    with pytest.raises(Exception):
        setup_mockdb.add_question(2)
