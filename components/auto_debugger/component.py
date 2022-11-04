from components.prompt import Prompt
from components.auto_debugger.completion_prompt import CompletionPrompt
from completion import Completion
from typing import Any
from components import utils

class AutoDebugger:
    def __init__(self, engine: str, max_completion_tokens: int, stream:bool):
        self.engine = engine
        self.stop = ["###"]
        self.stream: bool = stream
        self.max_completion_tokens: int = max_completion_tokens

    def debug(self, prompt: Prompt, temperature: float) -> Any:
        if isinstance(prompt, CompletionPrompt):
            completion = Completion.create(
                prompt=str(prompt),
                temperature=temperature,
                max_completion_tokens=self.max_completion_tokens,
                stop=self.stop,
                engine=self.engine,
                stream = self.stream
            )
            return utils.completion_text(completion, self.stream)     
        else:
            raise Exception(f"Unknown prompt type: {type(prompt)}")
