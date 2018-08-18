import pytest
from flask import url_for, jsonify
import json


def test_fetch_all(make_response_get_questions):
    data = json.loads(json.dumps(make_response_get_questions.json))
    assert make_response_get_questions.status_code == 200
    assert make_response_get_questions.json
    assert data['questions'][0]['title'] == "What is does Error 404 mean"
    assert len(data['questions']) > 2


def test_fetch_one(make_response_get_question, make_not_found):
    data = json.loads(json.dumps(make_response_get_question.json))
    assert make_response_get_question.status_code == 200
    assert make_response_get_question.json
    assert make_not_found.status_code == 404
    assert data['question']['title'] == "What does Error 400 mean"
    assert len(data['question']) == 3
