
import openai

openai.api_key = "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"

class AI:
    def __init__(self):
        pass
        

    def chat(self,prompt):
        prompt_tokens = len(prompt.split())
        max_tokens = 1024 + prompt_tokens
        print(max_tokens)
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        message = message.split("\n",1)[1]
        return message
