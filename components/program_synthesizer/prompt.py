from config import config
import utils
import os

class ProgramPrompt:
    def __init__(self, specification: str, old_program) -> None:
        path = os.path.join("components", "program_synthesizer")
        demo: str = utils.read_file(path, "template", "py").strip()
        self.prompt: str = f"{demo}\n"
        self.prompt += f"### Old\n{old_program}\n"
        self.prompt += f"### Specification\nChange the old program according to the following specification:\n{specification}\n"
        self.prompt += f"### New"

    def __str__(self) -> str:
        return self.prompt
