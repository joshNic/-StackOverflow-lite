from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# Sample data of questions
questions = [{
    "questionId": 1,
    "title" : "What is does Error 404 mean",
    "body" : "So i came across this when i was trying to access my old website"
}]


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'It works'})


@app.route('/questions', methods=['GET'])
def fetch_all():
    pass


@app.route('/question/<int:questionId>', methods=['GET'])
def fetch_one(questionId):
    pass

if __name__ == '__main__':
    app.run(debug=True, port=8080)
