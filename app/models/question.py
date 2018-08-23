from flask import request, abort, jsonify


class Question(object):

    def __init__(self):
        self.questionId = None
        self.title = None
        self.body = None
        self.questions = []

    def fetch_all_questions(self):
        return self.questions

    def fetch_single_question(self, questionId):
        question = [
            question for question in self.questions if
            question['questionId'] == questionId]
        if len(question) == 0:
            abort(404)
        if question:
            return question[0]

    def add_question(self, title, body):
        self.title = title
        self.body = body
        duplicate = [
            question for question in self.questions if question['title'] ==
            self.title
        ]
        if duplicate:
            return {'error': 'Question already exists'}
        if not self.questions:
            self.questionId = 1
        else:
            self.questionId = self.questions[-1]['questionId'] + 1
        question = {
            'questionId': self.questionId,
            'title': self.title,
            'body': self.body
        }
        self.questions.append(question)
        return question

    # def update_question():
    #     pass

    # def delete_question():
    #     pass
