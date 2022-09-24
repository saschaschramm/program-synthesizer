import os
import utils


class DebuggerPrompt:
    def __init__(self, program, error) -> None:
        self.program: str = program.strip()
        self.prompt_error: str = f"### {error.name}: {error.message}"
        auto_debugger_path = os.path.join("components", "auto_debugger")
        self.prompt: str = utils.read_file(auto_debugger_path, "template", "py").strip()

    def __str__(self) -> str:
        return f"{self.prompt}\n{self.program}\n{self.prompt_error}\n### Fixed Python"