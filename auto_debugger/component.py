
from completion import Completion
import utils
from verification_error import VerificationError

class AutoDebugger():

    def _prompt(self, code, error) -> str:
        prompt_error: str = f"### {error.name}: {error.message}"
        prompt: str = utils.read_file("auto_debugger", "prompt", "py")
        return f"{prompt.strip()}\n{code.strip()}\n{prompt_error}\n### Fixed Python"

    def debug(self, code: str, error: VerificationError) -> tuple[str]:
        prompt = self._prompt(code, error)
        completion: Completion = Completion(engine="code-davinci-002", 
                                        max_completion_tokens=1000, 
                                        temperature=0.0, 
                                        stop=["###"])
        return prompt, completion.create(prompt)

