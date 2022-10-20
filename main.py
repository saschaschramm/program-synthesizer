from logging import Logger
import os
import utils
from config import config
from components.auto_debugger.component import AutoDebugger
from components.program_synthesizer.component import ProgramSynthesizer
from components.verifier.component import Verifier
from components.verifier.verification_error import VerificationError
from components.prompt import Prompt

from components.program_synthesizer.completion_prompt import (
    CompletionPrompt as SynthesizerPrompt,
)
from components.auto_debugger.completion_prompt import (
    CompletionPrompt as DebuggerPrompt,
)
from logging_utils import get_logger

from program import Program

logger: Logger = get_logger()


def _specifications(filename: str) -> list[str]:
    lines = []
    with open(filename, mode="r", encoding="utf-8") as file:
        lines += file.readlines()
        # Ignore empty lines
        lines = [line for line in lines if line.strip() != ""]
        # Ignore comments
        lines = [line for line in lines if not line.startswith("#")]
        return [line.strip() for line in lines]


def main() -> None:
    ASSERTION_ERROR: str = "AssertionError"

    utils.make_dir(config.TMP_SYN_DIR)
    verifier: Verifier = Verifier()
    auto_debugger: AutoDebugger = AutoDebugger()
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer()
    program: str = utils.read_file(os.path.join(config.DATA_DIR, "main.py"))
    utils.write_file(os.path.join(config.TMP_SYN_DIR, "0000.py"), program.strip())
    specifications: list[str] = _specifications(config.SPEC_FILE)

    for index, specification in enumerate(specifications):
        base_filename: str = utils.filename(index + 1)
        logger.info(f"{base_filename} ---------------------------------")
        logger.info(f"Specification: {specification}")
        prompt: Prompt = SynthesizerPrompt(
            specification, program, template_file="template_test.py"
        )

        program, tests = program_synthesizer.synthesize(prompt, temperature=0.0)

        # We assume that the tests of the initial program are correct
        utils.write_file(os.path.join(config.TMP_SYN_DIR, f"{base_filename}.test"), tests)
        utils.write_file(os.path.join(config.TMP_SYN_DIR, f"{base_filename}.prompt"), str(prompt))
        utils.write_file(os.path.join(config.TMP_SYN_DIR, f"{base_filename}.py"), program)

        num_tries: int = 0
        max_tries: int = 3
        while num_tries < max_tries:
            verifier_program: Program = Program(program, timeout=3)
            try:
                verifier.verify(str(verifier_program))
                logger.info(f"Verification succeeded")
                break
            except VerificationError as error:
                logger.error(f"{error}")
                logger.info(f"Try {num_tries}")
                error_list: list[str] = str(error).split(":")
                if len(error_list) > 0:
                    error_type: str = error_list[0].strip()
                else:
                    error_type: str = str(error)

                if error_type == ASSERTION_ERROR:
                    # TODO This case is not triggered yet because the tests are not added to the program
                    prompt: Prompt = SynthesizerPrompt(
                        specification, program, template_file="template.py"
                    )
                    program, _ = program_synthesizer.synthesize(prompt, temperature=0.7)
                else:
                    # Tests are not generated again
                    prompt: Prompt = DebuggerPrompt(
                        program, error.message, template_file="template.py"
                    )
                    program = auto_debugger.debug(prompt, temperature=0.0)

                filename = f"{base_filename}-{num_tries}–{error_type}"
                utils.write_file(os.path.join(config.TMP_SYN_DIR, f"{filename}.prompt"), str(prompt))
                utils.write_file(os.path.join(config.TMP_SYN_DIR, f"{filename}.py"), program)

            except Exception as exception:
                print(exception)
                exit()
            
            num_tries += 1

if __name__ == "__main__":
    main()
