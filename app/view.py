from flask import Flask, jsonify, make_response, url_for, redirect
from .mockdbhelper import MockDBHelper

def create_app():
    qObject = MockDBHelper()
    app = Flask(__name__, instance_relative_config=True)
    app.config['TESTING'] = True
    app.config['DEBUG'] = True

    @app.route('/')
    def index():
        return redirect('https://stackv1.docs.apiary.io/#')
    
    # return all questions endpoint
    @app.route('/api/v1/questions', methods=['GET'])
    def fetch_all():
        return jsonify(qObject.fetch_all_questions())

    # get single question endpoint
    @app.route('/api/v1/question/<int:questionId>', methods=['GET'])
    def fetch_one(questionId):
        return jsonify(qObject.fetch_single_question(questionId))

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Question not found'}), 404)

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({"error": "Bad request check information again"}), 400)

    # get post question endpoint
    @app.route('/api/v1/question', methods=['POST'])
    def post_question():
        return jsonify(qObject.add_question()), 201

    # get post answer endpoint
    @app.route('/api/v1/question/<int:questionId>/answer', methods=['POST'])
    def add_answer(questionId):
        return jsonify(qObject.add_answer(questionId)), 201
    return app





