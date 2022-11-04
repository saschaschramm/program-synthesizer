import os.path
from logging import Logger
from typing import Optional
from components.auto_debugger.component import AutoDebugger
from components.auto_debugger.completion_prompt import (
    CompletionPrompt as DebuggerPrompt,
)
from components.program_synthesizer.component import ProgramSynthesizer
from components.explainer.component import Explainer
from components.verifier.component import Verifier
import utils
import synthesize_utils
from logging_utils import get_logger
from config import config

logger: Logger = get_logger()

SOURCE_DIR: str = config.DATA_DIR
TARGET_DIR: str = config.TMP_DEBUG_DIR
USE_SYN_TESTS: bool = False

if __name__ == "__main__":

    utils.make_dir(TARGET_DIR)
    tasks: dict = utils.read_file(os.path.join(SOURCE_DIR, "tasks-synthesized.json"))
    auto_debugger: AutoDebugger = AutoDebugger(config.ENGINE, 1000, stream=False)
    verifier: Verifier = Verifier()
    explainer: Explainer = Explainer()
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer(
        config.ENGINE, max_completion_tokens=500, stream=False
    )

    module_name: str = "main"

    for taskname, task in tasks.items():
        # if taskname != "HumanEval-18":
        #    continue
        logger.info(f"{taskname} ---------------------------------")        
        try_dir: str = os.path.join(TARGET_DIR, taskname, utils.filename(0))
        utils.make_dir(try_dir)
        utils.write_file(os.path.join(try_dir, "main.py"), task["program"])
        program: str = task["program_synthesized"]
        entry_point: str = task["entry_point"]
        specification: str = task["specification"]
        num_tries: int = 0
        max_tries: int = 3
        debugger_prompt: Optional[DebuggerPrompt] = None
        while num_tries < max_tries:
            if USE_SYN_TESTS:
                test = synthesize_utils.test(
                    module_name=module_name,
                    test=task["test_synthesized"],
                    entry_point=None,
                )
            else:
                test = synthesize_utils.test(
                    module_name=module_name,
                    test=task["test"],
                    entry_point=entry_point,
                )
            try_dir: str = os.path.join(TARGET_DIR, taskname, utils.filename(1), str(num_tries))
            utils.make_dir(try_dir)
            utils.write_files(try_dir, [("test.py", test), (f"{module_name}.py", program)])
            if debugger_prompt is not None:
                utils.write_file(
                    os.path.join(try_dir, f"debug_prompt.py"),
                    synthesize_utils.remove_line_number(str(debugger_prompt)),
                )

            success, command, stderr = verifier.verify(
                program,
                test=test,
                filename_program=f"{module_name}.py",
                filename_test="test.py",
            )
            if success:
                break
            else:
                logger.error(f"{stderr}")
                logger.info(f"{taskname} - try {num_tries}")
                last_line: str = synthesize_utils.last_line(stderr)
                # If stderr > 8000 then just use last line
                if len(stderr) > 8000:
                    error = last_line
                else:
                    error = stderr

                template_file, temperature = synthesize_utils.debugger_params(last_line)
                debugger_prompt = DebuggerPrompt(
                    specification=specification,
                    program=program,
                    error=error,
                    explanation=None,
                    template_file=template_file,
                    module_name=module_name,
                )
                program = auto_debugger.debug(debugger_prompt, temperature=temperature,)

            num_tries += 1
        task["program_debugged"] = program

    utils.write_json(os.path.join(config.TMP_DIR, "tasks-debugged.json"), tasks)
