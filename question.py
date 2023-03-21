from datetime import date

from templates.questionList import get_list_title_prompt
from templates.questionDetails import get_detail_prompt


class Question:

    def __init__(self, title: str,resources:str = "",category:str = "", questionLevel: str="Junior", capabilityLevel: str = "Qualified", areaId:str = 20 *"0", options=None,
                 correctAnswers=None):
        self.title = title
        self.category = category
        self.questionLevel = questionLevel
        self.type = "Theoretical"
        self.capabilityLevel = capabilityLevel
        self.options = options
        self.correctAnswers = correctAnswers
        self.author = "OpenAI"
        self.createdAt = date.today().strftime("%m/%d/%y")
        self.updatedAt = date.today().strftime("%m/%d/%y")
        self.resources = resources
        self.areaId = areaId
        print(f'Question {title} created')

    @staticmethod
    def get_list_title_prompt(scopes,count:int = 10, questionLevel:str = "Junior",  capabilityLevel:str = "Qualified" ):
        return get_list_title_prompt(scopes, count, questionLevel)

    @staticmethod
    def get_detail_prompt(title: str,questionLevel: str,):
        return get_detail_prompt(title,questionLevel)
    #
    # def add_index_correct_answer(self, correctAnswers):
    #     return [self.options.index(option) for option in self.options if option in correctAnswers]
