from components.prompt import Prompt
from components.auto_debugger.completion_prompt import CompletionPrompt
from completion import Completion


class AutoDebugger:
    def __init__(self):
        self.engine = "code-davinci-002"
        self.stop = ["###"]
        self.max_completion_tokens = 1000

    def debug(self, prompt: Prompt, temperature: float) -> str:
        if isinstance(prompt, CompletionPrompt):
            completion = Completion.create(
                prompt=str(prompt),
                temperature=temperature,
                max_completion_tokens=self.max_completion_tokens,
                stop=self.stop,
                engine=self.engine,
            )
            return completion["choices"][0]["text"].strip()
        else:
            raise Exception(f"Unknown prompt type: {type(prompt)}")
