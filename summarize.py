import openai
import os

def request_chatgpt(message, api_key, tokens) -> str:
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="You are a helpful assistant.\nUser: " + message,
        max_tokens=tokens
    )

    if response and response.choices:
        for choice in response.choices:
            return str(choice['text'])
    else:
        print("Error:", response['error']['message'])
