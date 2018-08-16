from flask import Flask, jsonify, request, Response, abort, make_response
app = Flask(__name__)

# Sample data of questions
questions = [{
    "questionId": 1,
    "title": "What is does Error 404 mean",
    "body": "So i came across this when i was trying to access my old website"
},
    {
    "questionId": 2,
    "title": "What does Error 401 mean",
    "body": "I have this application which always returns this error please help"
}]


@app.route('/api/v1', methods=['GET'])
def home():
    return jsonify({'message': 'It works'})

# return all questions endpoint
@app.route('/api/v1/questions', methods=['GET'])
def fetch_all():
    return jsonify({'questions': questions})

# get singl question endpoint
@app.route('/api/v1/question/<int:questionId>', methods=['GET'])
def fetch_one(questionId):
    question = [
        question for question in questions if question['questionId'] == questionId]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Question not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Please make sure that all fields are filled'}), 400)

@app.route('/api/v1/question', methods=['POST'])
def post_question():
    if not request.json or not 'title' in request.json or not 'body' in request.json:
        abort(400)
    question = {
        'questionId': questions[-1]['questionId'] + 1,
        'title': request.json.get('title', ""),
        'body': request.json.get('body', "")
    }
    questions.append(question)
    return jsonify({'question': question}), 201


if __name__ == '__main__':
    app.run(debug=True, port=8080)
