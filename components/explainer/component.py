from components.prompt import Prompt
from completion import Completion

# https://arxiv.org/pdf/2206.05802.pdf


class Explainer():

    def explain(self, prompt: Prompt, temperature: float, max_tokens: int) -> str:
        completion: dict = Completion.create(
                temperature=temperature,
                max_completion_tokens=max_tokens,
                stop=["### Specification"],
                engine="code-davinci-002",
                prompt=str(prompt),
                stream=False
        )
        text: str = completion["choices"][0]["text"].strip()
        return text


    