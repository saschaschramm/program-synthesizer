import os
from logging import Logger
import utils
from config import config
from components.program_synthesizer.component import ProgramSynthesizer
from components.test_synthesizer.component import TestSynthesizer
from components.verifier.component import Verifier
from components.auto_debugger.component import AutoDebugger
from components.test_synthesizer.completion_prompt import CompletionPrompt as TestPrompt

from components.prompt import Prompt

from components.program_synthesizer.completion_prompt import (
    CompletionPrompt as ProgramPrompt,
)
from components.auto_debugger.completion_prompt import (
    CompletionPrompt as DebuggerPrompt,
)

from logging_utils import get_logger
import synthesize_utils

logger: Logger = get_logger()


def _specifications(filename: str) -> list[str]:
    lines: list[str] = []
    with open(filename, mode="r", encoding="utf-8") as file:
        lines += file.readlines()
        # Ignore empty lines
        lines = [line for line in lines if line.strip() != ""]
        # Ignore comments
        lines = [line for line in lines if not line.startswith("#")]
        return [line.strip() for line in lines]


def main() -> None:
    module_name: str = "main"
    utils.make_dir(config.TMP_SYN_DIR)
    verifier: Verifier = Verifier()
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer(
        config.ENGINE, max_completion_tokens=500, stream=False
    )
    test_synthesizer: TestSynthesizer = TestSynthesizer(
        config.ENGINE, max_completion_tokens=500, stream=False
    )
    auto_debugger: AutoDebugger = AutoDebugger(config.ENGINE, 1000, stream=False)

    program_old: str = ""
    specifications: list[str] = _specifications(config.SPEC_FILE)

    for index, specification in enumerate(specifications):
        base_filename: str = utils.filename(index + 1)
        logger.info(f"{base_filename} ---------------------------------")
        logger.info(f"Specification: {specification}")
        program_prompt: Prompt = ProgramPrompt(
            specification, program_old, template_file="template.py"
        )
    
        program_new: str = program_synthesizer.synthesize(
            program_prompt, temperature=0.0
        )

        # We assume that the tests of the initial program are correct
        test_prompt: TestPrompt = TestPrompt(
            specification=specification,
            program_old=program_old,
            program_new=program_new,
            template_file="template.py",
        )
        program_old = program_new
        test: str = test_synthesizer.synthesize(test_prompt, temperature=0.0)
        test = synthesize_utils.test("main", test, None)
        
        tmp_dir: str = os.path.join(config.TMP_SYN_DIR, utils.filename(index), str(0))

        utils.make_dir(tmp_dir)
        utils.write_files(tmp_dir, [("test.py", test), ("prompt.py", str(program_prompt)), (f"{module_name}.py", program_new)])

        num_tries: int = 0
        max_tries: int = 3
        while num_tries < max_tries:
            success, _, stderr = verifier.verify(
                program_new,
                test=test,
                filename_program=f"{module_name}.py",
                filename_test="test.py",
            )
            if success:
                logger.info(f"Verification succeeded")
                break
            else:
                logger.error(f"{stderr}")
                logger.info(f"Try {num_tries}")

                last_line: str = synthesize_utils.last_line(stderr)
                template_file, temperature = synthesize_utils.debugger_params(last_line)

                debugger_prompt: DebuggerPrompt = DebuggerPrompt(
                    specification=specification,
                    program=program_new,
                    error=stderr,
                    explanation=None,
                    template_file=template_file,
                    module_name=module_name,
                )
                program_new: str = auto_debugger.debug(
                    debugger_prompt, temperature=temperature
                )

                tmp_dir: str = os.path.join(config.TMP_SYN_DIR, utils.filename(index), str(num_tries+1))
                utils.make_dir(tmp_dir)
                utils.write_files(tmp_dir, [("test.py", test), ("prompt.py", str(debugger_prompt)), (f"{module_name}.py", program_new)])

            num_tries += 1


if __name__ == "__main__":
    main()
