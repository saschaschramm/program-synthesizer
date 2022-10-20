from components.prompt import Prompt
import utils
import os


class CompletionPrompt(Prompt):
    def __init__(
        self, specification: str, program: str, template_file: str
    ) -> None:
        template_path: str = os.path.join("components", "program_synthesizer", template_file)
        template: str = utils.read_file(template_path).strip()
        if template_file == "template_test.py":
            self.prompt: str = template.format(specification=specification, program=program)
        elif template_file == "template.py":
            self.prompt: str = template.format(specification=specification, program=program)
        else:
            raise NotImplementedError(f"Template {template_file} not implemented")

    def __str__(self) -> str:
        return self.prompt
