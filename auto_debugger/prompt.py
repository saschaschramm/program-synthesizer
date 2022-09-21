import utils


class DebuggerPrompt:
    def __init__(self, code, error) -> None:
        self.code: str = code.strip()
        self.prompt_error: str = f"### {error.name}: {error.message}"
        self.prompt: str = utils.read_file("auto_debugger", "template", "py").strip()

    def __str__(self) -> str:
        return f"{self.prompt}\n{self.code}\n{self.prompt_error}\n### Fixed Python"