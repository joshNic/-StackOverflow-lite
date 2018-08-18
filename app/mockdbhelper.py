from flask import Flask, request, abort

# Sample data of questions
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

# Sample data of answers
ANSWERS = [{
    "answerId": 1,
    "questionId": 1,
    "answer_body": "It means error resource not found"
},
    {
    "answerId": 2,
    "questionId": 1,
    "answer_body": "It means what ever you are trying to find is not around"
},
    {
    "answerId": 3,
    "questionId": 2,
    "answer_body": "It means bad request"
},
    {
    "answerId": 4,
    "questionId": 2,
    "answer_body": "it means bad request check that your data is properly formated"
}]


class MockDBHelper(object):

    def fetch_all_questions(self):
        return {'questions': QUESTIONS}

    def fetch_single_question(self, questionId):
        question = [
            question for question in QUESTIONS if question['questionId'] == questionId]
        if len(question) == 0:
            abort(404)
        return {'question': question[0]}

    def add_question(self):
        if not request.json or not 'title' in request.json or not 'body' in request.json:
            abort(400)
        question = {
            'questionId': QUESTIONS[-1]['questionId'] + 1,
            'title': request.json.get('title', ""),
            'body': request.json.get('body', "")
        }
        QUESTIONS.append(question)
        return {'question': QUESTIONS}

    def add_answer(self, questionId):
        question = [
            question for question in QUESTIONS if question['questionId'] == questionId]
        if len(question) == 0:
            abort(404)
        if not request.json or not 'answer_body' in request.json:
            abort(400)
        if question:
            answer = {
                'answerId': ANSWERS[-1]['answerId'] + 1,
                'questionId': questionId,
                'answer_body': request.json.get('answer_body', "")
            }
            ANSWERS.append(answer)
        return {'answer': ANSWERS}
