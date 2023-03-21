from firestore import add_document_to_firestore
from openAI.airequest import get_questions_title, get_question_details
from question import Question


def generator(body):

    uncheckedlistTitles = get_questions_title(body["scopes"], body["questionCount"], body["questionLevel"])
    listTitles = []

    for item in uncheckedlistTitles:
        try:
            opt = eval(item)
            listTitles.append(opt)
        except:
            continue
    questions = [Question(item[1], item[2], item[0], body["questionLevel"], body["capabilityLevel"], body["areaId"]) for
                 item in listTitles if item[1].strip() not in body["scopes"]]
    failed = []
    for question in questions:
        answer = get_question_details(question.title, question.questionLevel)
        try:
            answer = eval(answer)
            question.correctAnswers = [int(answer["Correct answer"])]
            answer.pop("Correct answer")
            question.options = list(answer.values())
            add_document_to_firestore(question, body["prefix"])
        except:
            failed.append(question.title)
            print("An exception occurred: Fail parse options")
        add_document_to_firestore(question, body["prefix"])
        #print(question.__dict__)
    return [item for item in questions if item.title not in failed]