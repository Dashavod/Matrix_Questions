from templates.questionList import get_list_title_prompt
from templates.questionDetails import get_detail_prompt


class Question:

    def __init__(self, title: str, questionLevel: str, capabilityLevel: str = "Qualified", options=None,
                 correctAnswers=None):
        self.title = title
        self.questionLevel = questionLevel
        self.type = "Theoretical"
        self.capabilityLevel = capabilityLevel
        self.options = options
        self.correctAnswers = correctAnswers
        print(f'Question {title} created')

    @staticmethod
    def get_list_title_prompt(count: int, questionLevel: str, scopes, capabilityLevel: str = "Qualified"):
        return get_list_title_prompt(count, questionLevel, scopes)

    @staticmethod
    def get_detail_prompt(title: str,questionLevel: str,):
        return get_detail_prompt(title,questionLevel)
    #
    # def add_index_correct_answer(self, correctAnswers):
    #     return [self.options.index(option) for option in self.options if option in correctAnswers]
