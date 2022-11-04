from components.prompt import Prompt
import utils
import os


class CompletionPrompt(Prompt):
    def __init__(
        self, specification: str, program: str, template_file: str, module_name: str, error: str
    ) -> None:
        template_path: str = os.path.join("components", "explainer", template_file)
        template: str = utils.read_file(template_path).strip()
        if template_file == "template.py":
            self.prompt: str = template.format(specification=specification, program=program, module_name=module_name, error=error)
        else:
            raise NotImplementedError(f"Template {template_file} not implemented")

    def __str__(self) -> str:
        return self.prompt
