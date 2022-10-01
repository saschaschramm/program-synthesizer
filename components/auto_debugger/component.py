import os
from typing import Optional

from components.auto_debugger.prompt import DebuggerPrompt
from components.verifier.verification_error import VerificationError
from completion import Completion
from config import config
import utils


class AutoDebugger:
    def __init__(self) -> None:
        #self.path = path
        self.completion: Completion = Completion(
            engine="code-davinci-002",
            max_completion_tokens=1000,
            temperature=0.0,
            stop=["###"],
        )

    def debug(
        self, program: str, error: VerificationError, dir: str, name: Optional[str]
    ) -> str:
        prompt: DebuggerPrompt = DebuggerPrompt(
            program, error.message, include_error=True
        )
        if name is not None:
            utils.write_file(os.path.join(dir, f"{name}.prompt"), str(prompt))
            utils.write_file(os.path.join(dir, f"{name}.py"),
                program.strip(),
            )
        return self.completion.create(str(prompt)).strip()
