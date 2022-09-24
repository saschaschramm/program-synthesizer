from completion import Completion
from components.program_synthesizer.prompt import ProgramPrompt
from config import config


class ProgramSynthesizer:
    def synthesize(self, specification: str, old_program: str) -> tuple[str]:
        prompt: str = ProgramPrompt(specification, old_program)
        completion: Completion = Completion(
            engine="code-davinci-002",
            max_completion_tokens=config.NUM_TOKENS,
            temperature=0.0,
            stop=["###", "## Change"],
        )
        text: str = completion.create(str(prompt)).strip()
        return prompt, text
