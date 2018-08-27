import pytest
from app.views import app as create_app
import json


@pytest.fixture
def app():
    app = create_app
    app.debug = True
    return app


@pytest.fixture
def make_response_post_question(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = {
        'title': 'what does 404 mean',
        'body': 'Means resoce not found'
    }
    url = '/api/v1/question'
    response = client.post(url, data=json.dumps(data), headers=headers)
    yield response


@pytest.fixture
def make_response_get_question(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    url = '/api/v1/question/2'
    response = client.get(url, headers=headers)
    yield response


@pytest.fixture
def make_response_get_questions(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    url = '/api/v1/questions'
    response = client.get(url, headers=headers)
    yield response


@pytest.fixture
def make_response_post_answer(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = {
        'answer_body': 'Means resources you look for not availbale not found'
    }
    url = '/api/v1/question/1/answer'
    response = client.post(url, data=json.dumps(data), headers=headers)
    yield response


@pytest.fixture
def make_bad_request(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = {
        'answer_body': 'Means resources you look for not availbale not found'
    }
    url = '/api/v1/question/2/answer'
    response = client.post(url, data=data, headers=headers)
    yield response


@pytest.fixture
def make_not_found(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = {
        'answer_body': 'Means resources you look for not availbale not found'
    }
    url = '/api/v1/question/90/answer'
    response = client.post(url, data=json.dumps(data), headers=headers)
    yield response


@pytest.fixture
def home_response(client):
    url = '/'
    response = client.get(url)
    yield response


@pytest.fixture
def validate_response(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = {
        'answer_body': 'Means resources you look for not availbale not found'
    }
    url = '/api/v1/question/3/answer'
    response = client.post(url, data=json.dumps(data), headers=headers)
    yield response
