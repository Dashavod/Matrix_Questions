def get_detail_prompt(title:str,questionLevel:str = "Middle"):
    """Get Titles
    Args:
       title (str): title nessesary question.
       questionLevel(str): default value "Middle"
       Returns:
        return prompt with params
    """
    example = {
           "0": " Number, Boolean, String, Float, Undefined",
            "1": "Number, Boolean, String, Double, Undefined ",
            "2": "Int, Boolean, Text, Null, Data",
            "3": "Number, Boolean, String, Null, Undefined",
            "Correct answer": "3 "
 }
    return f"""  
        Imagine you are  senior frontend developer, you need interviewing by test {questionLevel}-level developer,  you have  question: What are the different data types available in JavaScript? with this options:
        {example} 
        give me options strongly only in following format and mark correct answer like in example for question {title}
    """