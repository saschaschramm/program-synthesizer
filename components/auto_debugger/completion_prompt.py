import os
import utils

from components.prompt import Prompt


class CompletionPrompt(Prompt):
    def __init__(
        self, program: str, error: str, template_file: str
    ) -> None:
        self.program: str = program.strip()
        self.prompt_error: str = error
        auto_debugger_path: str = os.path.join("components", "auto_debugger")
        self.template: str = utils.read_file(os.path.join(auto_debugger_path, template_file)).strip()
        self.template_file: str = template_file

    def __str__(self) -> str:
        if self.template_file == "template.py":
            return self.template.format(program=self.program, error=self.prompt_error)
        else:
            raise NotImplementedError
