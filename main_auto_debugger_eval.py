from logging import Logger
from components.auto_debugger.component import AutoDebugger
from components.program_synthesizer.component import ProgramSynthesizer
from components.prompt import Prompt
from components.verifier.component import Verifier
from components.verifier.component import VerificationError
import utils
import os.path
from logging_utils import get_logger
from config import config
from program import Program


from components.program_synthesizer.completion_prompt import (
    CompletionPrompt as SynthesizerPrompt,
)
from components.auto_debugger.completion_prompt import (
    CompletionPrompt as DebuggerPrompt,
)

logger: Logger = get_logger()


ASSERTION_ERROR: str = "AssertionError"


if __name__ == "__main__":
    SOURCE_DIR: str = config.TMP_DIR
    TARGET_DIR: str = config.TMP_DEBUG_DIR
    USE_SYN_TESTS = False

    utils.make_dir(TARGET_DIR)
    tasks: dict = utils.read_file(os.path.join(SOURCE_DIR, "tasks-synthesized.json"))
    auto_debugger: AutoDebugger = AutoDebugger()
    verifier: Verifier = Verifier()
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer()

    for taskname, task in tasks.items():
        logger.info(f"{taskname} ---------------------------------")
        taskname: str = taskname.replace("/", "-")
        tmp_task_dir: str = os.path.join(config.TMP_DEBUG_DIR, taskname)
        utils.make_dir(tmp_task_dir)
        utils.write_file(
            os.path.join(tmp_task_dir, f"{utils.filename(0)}.py"), task["program"]
        )
        program: str = task["program_synthesized"]
        entry_point: str = task["entry_point"]
        specification: str = task["specification"]

        if USE_SYN_TESTS:
            tests: str = task["test_synthesized"]
        else:
            tests = task["test"]

        num_tries: int = 0
        max_tries: int = 3
        while num_tries < max_tries:
            verifier_program = Program(program, timeout=3)

            if USE_SYN_TESTS:
                verifier_program.add_syn_tests(tests, entry_point)
            else:
                verifier_program.add_tests(tests, entry_point)

            try:
                path_executable: str = os.path.join(
                    TARGET_DIR, taskname, f"{utils.filename(1)}-{num_tries}-exec.py"
                )
                utils.write_file(path_executable, str(verifier_program))
                command: str = verifier.verify(str(verifier_program))
                logger.info(f"Verification succeeded – {command}")
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
                    prompt: Prompt = SynthesizerPrompt(
                        specification, program, template_file="template.py"
                    )
                    program, _ = program_synthesizer.synthesize(prompt, temperature=0.7)
                else:
                    prompt: Prompt = DebuggerPrompt(
                        program, error.message, template_file="template.py"
                    )
                    program = auto_debugger.debug(prompt, temperature=0.0)

                name = f"{utils.filename(1)}-{num_tries}–{error_type}"
                utils.write_file(
                    os.path.join(TARGET_DIR, taskname, f"{name}.prompt"), str(prompt)
                )
            except Exception as exception:
                logger.error(f"Unexpected error: {exception}")
                exit()
            num_tries += 1
        task["program_debugged"] = program

    utils.write_json(os.path.join(config.TMP_DIR, "tasks-debugged.json"), tasks)
