from flask import abort

from service import generator


def questionGenerator(request):

    body = request.get_json(force=True, silent=True,
                            cache=True)

    if body.get("scopes") is None:
        return abort(400, "Expected parameter 'scopes'")

    questions,failed = generator(body)
    response = {
        "countAddedQuestions": len(questions),
        "result": "Success"
    }
    if not failed: response["failed"] = failed
    return response
