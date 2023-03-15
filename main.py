import os

from flask import abort
from firestore import add_document_to_firestore
from openAI.airequest import get_questions_title, get_question_details
from question import Question


def getquestions(request):

    body = request.get_json(force=True, silent=True,
                            cache=True)

    if body.get("scopes") is None:
        return abort(400, "Expected parameter 'scopes'")


    uncheckedlistTitles = get_questions_title(body["scopes"], body["questionCount"], body["questionLevel"])
    listTitles = []

    for item in uncheckedlistTitles:
        try:
            opt = eval(item)
            listTitles.append(opt)
        except:
            continue
    questions = [Question(item[1], item[2], item[0], body["questionLevel"], body["capabilityLevel"], body["areaId"]) for
                 item in listTitles]
    failed = []
    for question in questions:
        answer = get_question_details(question.title, question.questionLevel)
        try:
            answer = eval(answer)
            question.correctAnswers = [int(answer["Correct answer"])]
            answer.pop("Correct answer")
            question.options = list(answer.values())
            add_document_to_firestore(question, "ai")
        except:
            failed.append(question.title)
            print("An exception occurred: Fail parse options")
        print(question.__dict__)
    response = [item for item in questions if item.title not in failed]
    return {
        "countAddedQuestions": len(response),
        "result": "Success"
    }
