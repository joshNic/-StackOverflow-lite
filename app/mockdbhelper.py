from flask import request, abort, jsonify

# Sample data of questions
QUESTIONS = []

# Sample data of answers
ANSWERS = []


class MockDBHelper(object):

    def fetch_all_questions(self):
        return {'questions': QUESTIONS}

    def fetch_single_question(self, questionId):
        question = [
            question for question in QUESTIONS if
            question['questionId'] == questionId]
        answer = [
            answer for answer in ANSWERS if answer['questionId'] == questionId]
        if len(question) == 0:
            abort(404)
        return {'question': question[0], 'answers': answer}

    def add_question(self):
        if not request.json:
            abort(400)
        if 'title' not in request.json:
            return {'error': 'please title is required'}
        if 'body' not in request.json:
            return {'error': 'please body is required'}
        duplicate = [
            question for question in QUESTIONS if question['title'] ==
            request.json.get('title', "")
        ]
        if duplicate:
            return {'error': 'Question already exists'}
        if not QUESTIONS:
            id = 1
        else:
            id = QUESTIONS[-1]['questionId'] + 1
        question = {
            'questionId': id,
            'title': request.json.get('title', ""),
            'body': request.json.get('body', "")
        }
        QUESTIONS.append(question)
        return {'question': question, 'message': 'Question successfully added'}

    def add_answer(self, questionId):
        question = [
            question for question in QUESTIONS if
            question['questionId'] == questionId]
        if len(question) == 0:
            abort(404)
        if not request.json:
            abort(400)
        if 'answer_body' not in request.json:
            return {'error': 'Please answer field can not be empty'}
        if question:
            if not ANSWERS:
                answerId = 1
            else:
                answerId = ANSWERS[-1]['answerId'] + 1
            answer = {
                'answerId': answerId,
                'questionId': questionId,
                'answer_body': request.json.get('answer_body', "")
            }
            ANSWERS.append(answer)
        return {'answer': answer, 'message': 'Answer successfully added'}
