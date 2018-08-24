import pytest
from flask import url_for, jsonify
import json


# def test_bad_request(make_bad_request):
#     data = json.loads(json.dumps(make_bad_request.json))
#     assert make_bad_request.status_code == 400
#     # assert make_bad_request.json
#     # assert data['error'] == 'Bad request check information again'


def test_not_found(make_not_found):
    data = json.loads(json.dumps(make_not_found.json))
    assert make_not_found.status_code == 404
    assert make_not_found.json
    assert data['error'] == 'Question not found'


def test_index(home_response):
    assert home_response.status_code == 302


def test_fetch_all(make_response_get_questions):
    data = json.loads(json.dumps(make_response_get_questions.json))
    assert make_response_get_questions.status_code == 200
    assert isinstance(make_response_get_questions.json, list)
    
    assert len(data[0]) == 3
    with pytest.raises(TypeError):
        assert data['questions'][0]['title'] == "what does 404 mean"


def test_fetch_one(make_response_get_question, make_not_found):
    data = json.loads(json.dumps(make_response_get_question.json))
    assert make_response_get_question.status_code == 200
    assert make_response_get_question.json
    assert make_not_found.status_code == 404


def test_post_question(make_response_post_question, make_bad_request):
    assert make_response_post_question.status_code == 201
    assert make_response_post_question.json
    assert make_bad_request.status_code == 400


def test_add_answer(
    make_response_post_answer, make_bad_request, make_not_found
):
    assert make_response_post_answer.status_code == 201
    assert make_response_post_answer.json
    assert make_bad_request.status_code == 400
    assert make_not_found.status_code == 404


