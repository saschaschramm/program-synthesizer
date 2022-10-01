import os

from completion import Completion
from components.program_synthesizer.prompt import ProgramPrompt
from config import config

import utils


class ProgramSynthesizer:

    def __init__(self, program_dir) -> None:
        self.program_dir: str = program_dir
        utils.make_dir(program_dir)


    def synthesize(self, specification: str, old_program: str, name: str) -> str:
        prompt: str = ProgramPrompt(specification, old_program)
        completion: Completion = Completion(
            engine="code-davinci-002",
            max_completion_tokens=config.NUM_TOKENS,
            temperature=0.0,
            stop=["###"],
        )
        program: str = completion.create(str(prompt)).strip()
        utils.write_file(os.path.join(self.program_dir, f"{name}.prompt"), str(prompt))
        utils.write_file(os.path.join(self.program_dir, f"{name}.py"), program)
        return program
