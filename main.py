import os

from openAI.airequest import get_questions_title, get_question_details
from question import Question


def getquestions(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    body = request.get_json(force=True, silent=True,
                            cache=True)  # see https://flask.palletsprojects.com/en/2.0.x/api/ get_json Parse data as JSON
    listTitles = get_questions_title(body["questionCount"], body["questionLevel"], body["scopes"])
    listTitles = [item[3:] for item in listTitles if item and item not in body["scopes"]]
    questions = [Question(title.strip(), body["questionLevel"]) for title in listTitles]
    for question in questions:
        answer = get_question_details(question.title,question.questionLevel)
        answer = eval(answer)
        question.correctAnswers = [int(answer["Correct answer"])]
        answer.pop("Correct answer")
        question.options = list(answer.values())
        print(question.__dict__)

    return [question.__dict__ for question in questions ]
