def get_list_title_prompt(scopes,count:int = 10, questionLevel:str = "Junior",  capabilityLevel:str = "Qualified" ):
    """Get Titles
    Args:
        count(int): question count request for generating
        questionLevel(str): question level for question
        scopes(list): category for question generating
        capabilityLevel(str): grading in each level, default value "Qualified", also can be "Master", "Competent"
    Returns:
        return prompt with params
    """
    example1 = ["HTML", "What is the difference between HTML and XHTML?","https://developer.mozilla.org/en-US/docs/Web/HTML"]
    example2 = 	["React","What is the purpose of the React component lifecycle?","https://reactjs.org/docs/react-component.html"]
    return f"Imagine you a senior frontend developer give me {count} unusual question for test, with this categories {scopes} for interviewing developer {questionLevel} level developer, only question with categories without answers, answer for your question must be short, without numeration and following this format\n{example1}\n{example2}\ngenerate {count} questions in this format with this categories"