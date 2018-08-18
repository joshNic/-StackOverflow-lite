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
