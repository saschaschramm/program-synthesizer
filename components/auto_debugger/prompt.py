import os
import utils


class DebuggerPrompt:
    def __init__(
        self, program: str, error: str, include_error: bool
    ) -> None:
        self.program: str = program.strip()
        self.include_error: bool = include_error
        self.prompt_error: str = f"### {error}"
        auto_debugger_path: str = os.path.join("components", "auto_debugger")
        if include_error:
            self.prompt: str = utils.read_file(os.path.join(auto_debugger_path, "template.py")).strip()
        else:
            self.prompt: str = utils.read_file(os.path.join(auto_debugger_path, "template_no_error.py")).strip()

    def __str__(self) -> str:
        if self.include_error:
            return (
                f"{self.prompt}\n{self.program}\n{self.prompt_error}\n### Fixed Python"
            )
        else:
            return f"{self.prompt}\n{self.program}\n### Fixed Python"
