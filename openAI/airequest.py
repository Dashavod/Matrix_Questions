from openAI.kernel import kernel
from question import Question


def get_questions_title(count: int, questionLevel: str, scopes, capabilityLevel: str = "Qualified"):
    """Get Titles
    Args:
        count(int): question count request for generating
        questionLevel(str): question level for question
        scopes(list): category for question generating
        capabilityLevel(str): grading in each level, default value "Qualified", also can be "Master", "Competent"
    Returns:
        return list of str with question titles
    """
    prompt = Question.get_list_title_prompt(count, questionLevel, scopes)
    return kernel(prompt,"daria",0.27).split("\n")


def get_question_details(title: str, questionLevel: str = "Middle"):
    """Get Answers
    Args:
        title (str): title nessesary question.
        questionLevel(str): question level for question, default value Middle

    Returns:
        return dictionary with options and correctAnswer
       """
    prompt = Question.get_detail_prompt(title,questionLevel)
    return kernel(prompt,"daria",0.27)
