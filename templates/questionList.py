def get_list_title_prompt(count:int, questionLevel:str, scopes, capabilityLevel:str = "Qualified" ):
    """Get Titles
    Args:
        count(int): question count request for generating
        questionLevel(str): question level for question
        scopes(list): category for question generating
        capabilityLevel(str): grading in each level, default value "Qualified", also can be "Master", "Competent"
    Returns:
        return prompt with params
    """
    return f"Imagine you a senior frontend developer give me {count} unusual question for test, with this categories {scopes} for interviewing developer {questionLevel} level, only question without answers, answer for your question must be short"