import os

import openai
from dotenv import dotenv_values

SENSITIVE_DATA = 'You request contans sensitive data. Please change request'

# for google function os.getenv('OPENAI_API_TOKEN')
# for local  dotenv_values("env/.env")['OPENAI_API_TOKEN']
openai_api_key = os.getenv('OPENAI_API_TOKEN') if os.getenv('OPENAI_API_TOKEN') else dotenv_values("env/.env")['OPENAI_API_TOKEN']


ENGINE_NAME = 'text-davinci-003'
openai.api_key = openai_api_key


def kernel(
    prompt: str,
    user_id: str,
    temp: float,
    max_tokens=500,
    min_output=50,
    max_tries=3,
    presence_penalty=0.0,
    frequency_penalty=0.0,
    stop_words=None,
    disable_filter=False
) -> str:
    tries = 0

    while tries < max_tries:
        resp = openai.Completion.create(
            user=user_id,
            engine=ENGINE_NAME,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temp,
            top_p=1,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop_words
        )

        tries = tries + 1
        print(resp)
        choices = resp['choices']
        if len(choices) > 0:
            result = choices[0]['text'].strip()
            return result

    return ''
