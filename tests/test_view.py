import pytest
from flask import url_for, jsonify
import json


def test_fetch_all(make_response_get_questions):
    data = json.loads(json.dumps(make_response_get_questions.json))
    assert make_response_get_questions.status_code == 200
    assert make_response_get_questions.json
    assert data['questions'][0]['title'] == "What is does Error 404 mean"
    assert len(data['questions']) > 2
