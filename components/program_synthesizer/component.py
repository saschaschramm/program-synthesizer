from completion import Completion

from components.program_synthesizer.completion_prompt import CompletionPrompt
from components.prompt import Prompt
from typing import Any
from components import utils



class ProgramSynthesizer:
    def __init__(self, engine: str, max_completion_tokens: int, stream: bool) -> None:
        self.engine: str = engine
        self.max_completion_tokens = max_completion_tokens
        self.stream = stream

    def synthesize(self, prompt: Prompt, temperature: float) -> Any:
        if isinstance(prompt, CompletionPrompt):
            completion: Any = Completion.create(
                temperature=temperature,
                max_completion_tokens=self.max_completion_tokens,
                stop=["\n###"],
                engine=self.engine,
                prompt=str(prompt),
                stream=self.stream
            )
            return utils.completion_text(completion, self.stream)
        else:
            raise Exception(f"Unknown prompt type: {type(prompt)}")

