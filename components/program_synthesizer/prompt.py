import utils
import os

class ProgramPrompt:
    def __init__(self, specification: str, old_program) -> None:
        template_path: str = os.path.join("components", "program_synthesizer", "template.py")
        demo: str = utils.read_file(template_path).strip()
        self.prompt: str = f"{demo}\n"
        self.prompt += f"### Old\n{old_program}\n"
        self.prompt += f"### Specification\nChange the old program according to the following specification:\n{specification}\n"
        self.prompt += f"### New"

    def __str__(self) -> str:
        return self.prompt
