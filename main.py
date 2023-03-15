from flask import abort

from service import generator


def questionGenerator(request):

    body = request.get_json(force=True, silent=True,
                            cache=True)

    if body.get("scopes") is None:
        return abort(400, "Expected parameter 'scopes'")

    response = generator(body)
    return {
        "countAddedQuestions": len(response),
        "result": "Success"
    }
