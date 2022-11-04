import os
import utils

from components.prompt import Prompt
from typing import Optional


class CompletionPrompt(Prompt):
    def __init__(
        self,
        specification: Optional[str],
        program: str,
        error: str,
        explanation: Optional[str],
        template_file: str,
        module_name: str
    ) -> None:
        self.program: str = program.strip()
        self.error: str = error
        auto_debugger_path: str = os.path.join("components", "auto_debugger")
        self.template: str = utils.read_file(
            os.path.join(auto_debugger_path, template_file)
        ).strip()
        self.template_file: str = template_file
        self.explanation: Optional[str] = explanation
        self.specification: Optional[str] = specification
        self.module_name: str = module_name

    def __str__(self) -> str:
        if self.template_file == "template_interpreter.py":
            return self.template.format(
                program=self.program,
                error=self.error,
                module_name=self.module_name,
            )
        elif self.template_file == "template_assertion_explain.py":
            return self.template.format(
                specification=self.specification,
                program=self.program,
                error=self.error,
                explanation=self.explanation,
                module_name=self.module_name,
            )
        elif self.template_file == "template_assertion.py" or self.template_file == "template_assertion_test.py":
            return self.template.format(
                program=self.program,
                error=self.error,
                specification=self.specification,
                module_name=self.module_name,
            )
        else:
            raise NotImplementedError
