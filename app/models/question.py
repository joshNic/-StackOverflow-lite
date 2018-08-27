from flask import request, abort, jsonify

questions = []


class Question(object):

    def __init__(self):
        self.questionId = None
        self.title = None
        self.body = None

    def fetch_all_questions(self):
        return questions

    def fetch_single_question(self, questionId):
        question = [
            question for question in questions if
            question['questionId'] == questionId]
        if len(question) == 0:
            abort(404)
        if question:
            return question[0]

    def add_question(self, title, body):
        self.title = title
        self.body = body
        duplicate = [
            question for question in questions if question['title'] ==
            self.title
        ]
        if len(self.title) < 6:
            return {'error': 'Question title can not be less than six\
            characters'}
        if len(self.body) < 6:
            return {'error': 'Question body can not be less than six\
            characters'}
        if self.title.isdigit():
            return {'error': 'Question format not allowed\
            a question title can not only have numbers'}
        if self.body.isdigit():
            return {'error': 'Question format not allowed\
            a question body can not only have numbers'}
        if duplicate:
            return {'error': 'Question already exists'}
        if not questions:
            self.questionId = 1
        else:
            self.questionId = questions[-1]['questionId'] + 1
        question = {
            'questionId': self.questionId,
            'title': self.title,
            'body': self.body
        }
        questions.append(question)
        return question

    # def update_question():
    #     pass

    # def delete_question():
    #     pass
