from flask import (
    Flask, jsonify, make_response, redirect, json, Response, request
)
from app import create_app
from .models.question import Question
from .models.answer import Answer

questionObject = Question()
answerObject = Answer()


app = create_app()


@app.route('/')
def index():
    return redirect('https://stackv1.docs.apiary.io/#')


# return all questions endpoint
@app.route('/api/v1/questions', methods=['GET'])
def fetch_all():
    return jsonify(questionObject.fetch_all_questions())


# get single question endpoint
@app.route('/api/v1/question/<int:questionId>', methods=['GET'])
def fetch_one(questionId):
    questions = questionObject.fetch_single_question(questionId)
    if questions:
        return jsonify({
            'Question': questions,
            'Answers': answerObject.get_answers(questionId)
        })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Question not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({
        "error": "Bad request check information again"}), 400)


# get post question endpoint
@app.route('/api/v1/question', methods=['POST'])
def post_question():
    request_data = request.get_json()
    if not validate_question_object(request_data):
        title = request_data['title']
        body = request_data['body']
        return jsonify(questionObject.add_question(title, body)), 201


# get post answer endpoint
@app.route('/api/v1/question/<int:questionId>/answer', methods=['POST'])
def add_answer(questionId):
    request_data = request.get_json()
    if not validate_answer_object(request_data):
        answer_body = request_data['answer_body']
        return jsonify(
            answerObject.add_answer(questionId, answer_body)), 201


def validate_question_object(request_object):
    if not request_object:
        abort(400)
    if 'title' not in request_object:
        return {'error': 'please title is required'}
    if 'body' not in request_object:
        return {'error': 'please body is required'}


def validate_answer_object(request_object):
    if not request_object:
        abort(400)
    if 'answer_body' not in request_object:
        return {'error': 'please answer can not be empty'}
