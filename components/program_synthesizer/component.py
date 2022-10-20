from completion import Completion
from components.program_synthesizer.completion_prompt import CompletionPrompt
from components.prompt import Prompt
from config import config


class ProgramSynthesizer:
    def __init__(self) -> None:
        self.synthesize_tests: bool = True

    def synthesize(self, prompt: Prompt, temperature) -> tuple[str, str]:
        if isinstance(prompt, CompletionPrompt):
            completion: dict = Completion.create(
                temperature=temperature,
                max_completion_tokens=config.NUM_TOKENS,
                stop=["### Old"],
                engine="code-davinci-002",
                prompt=str(prompt),
            )

            if self.synthesize_tests:
                text = completion["choices"][0]["text"].strip()
                group = text.split("### Tests (max 5)")
                program = group[0].strip()
                if len(group) > 1:
                    tests = group[1].strip()
                else:
                    tests = ""
            else:
                program: str = completion["choices"][0]["text"].strip()
                tests = ""

            return program, tests
        else:
            raise Exception(f"Unknown prompt type: {type(prompt)}")
