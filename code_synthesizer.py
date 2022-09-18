import utils
from completion import Completion
from config import config

class CodeSynthesizer():

    def _prompt(self, specification: str, old_tag: str, new_tag: str) -> str:
        program: str = utils.read_file(config.PROGRAM_DIR, "main", "py").strip()
        prompt: str = ""
        specification: str = f"Change the old program according to the following specification:\n{specification}"
        for (tag, value) in [(old_tag, program), ("specification", specification)]:
            prompt += f"<{tag}>\n{value}\n</{tag}>\n"
        prompt += f"<{new_tag}>"
        return prompt

    def synthesize(self, specification: str, old_name: str, new_name: str) -> tuple[str]:
        prompt: str = self._prompt(specification, old_name, new_name)
        completion: Completion = Completion(engine="code-davinci-002", max_completion_tokens=400, temperature=0.0, stop=[f"</{new_name}>"])
        text: str = completion.create(prompt).strip()
        return prompt, text