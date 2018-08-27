from flask import request, abort, jsonify
from .question import Question

questionObject = Question()

answers = []


class Answer(object):

    def __init__(self):
        self.answerId = None
        self.questionId = None
        self.answer_body = None

    def get_answers(self, questionId):
        self.questionId = questionId
        answer = [
            answer for answer in answers if answer['questionId'] ==
            self.questionId]
        return answer

    def add_answer(self, questionId, answer_body):
        self.questionId = questionId
        self.answer_body = answer_body
        check = questionObject.fetch_single_question(self.questionId)
        if check:
            if not answers:
                self.answerId = 1
            else:
                self.answerId = answers[-1]['answerId'] + 1
            answer = {
                'answerId': self.answerId,
                'questionId': self.questionId,
                'answer_body': self.answer_body
            }
            answers.append(answer)
            return answer

    # def update_answer(self):
    #     pass

    # def delete_answer(self):
    #     pass
