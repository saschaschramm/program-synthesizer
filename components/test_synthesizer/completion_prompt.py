from components.prompt import Prompt
import utils
import os


class CompletionPrompt(Prompt):
    def __init__(
        self, specification: str, program_old: str, program_new: str, template_file: str
    ) -> None:
        template_path: str = os.path.join("components", "test_synthesizer", template_file)
        template: str = utils.read_file(template_path).strip()

        if template_file == "template.py":
            self.prompt: str = template.format(
                specification=specification, 
                program_old=program_old,
                program_new=program_new)
        else:
            raise NotImplementedError(f"Template {template_file} not implemented")

    def __str__(self) -> str:
        return self.prompt