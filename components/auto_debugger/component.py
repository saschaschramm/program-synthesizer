
from components.auto_debugger.prompt import DebuggerPrompt
from components.verifier.verification_error import VerificationError
from completion import Completion

class AutoDebugger():

    def __init__(self):
        self.completion: Completion = Completion(engine="code-davinci-002", 
                                        max_completion_tokens=1000, 
                                        temperature=0.0, 
                                        stop=["###"])

    def debug(self, code: str, error: VerificationError) -> tuple[str]:
        prompt = DebuggerPrompt(code, error)    
        return prompt, self.completion.create(str(prompt)).strip()

