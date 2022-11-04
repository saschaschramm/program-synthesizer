from logging import Logger
from components.explainer.completion_prompt import CompletionPrompt as ExplainerPrompt
from components.explainer.component import Explainer

from components.verifier.component import Verifier
from components.auto_debugger.component import AutoDebugger


from config import config
import utils

import synthesize_utils

import os

from logging_utils import get_logger

logger: Logger = get_logger()

from components.auto_debugger.completion_prompt import (
    CompletionPrompt as DebuggerPrompt,
)


if __name__ == "__main__":
    SOURCE_DIR: str = config.DATA_DIR
    TARGET_DIR: str = os.path.join("tmp", "explain")
    utils.make_dir(TARGET_DIR)

    OPTION = ("program_synthesized", "tasks-synthesized.json")

    tasks: dict = utils.read_file(os.path.join(SOURCE_DIR, OPTION[1]))

    verifier: Verifier = Verifier()
    explainer = Explainer()

    for taskname, task in tasks.items():
        entry_point: str = task["entry_point"]
        taskname: str = taskname.replace("/", "-")

        if taskname != "HumanEval-5":
            continue

        print(taskname)

        # print(entry_point)
        program: str = task[OPTION[0]]
        specification: str = task["specification"]
        print(specification)

        test: str = task["test"]

        num_tries: int = 0
        max_tries: int = 3

        tmp_dir = os.path.join(TARGET_DIR, taskname)
        utils.make_dir(tmp_dir)

        auto_debugger: AutoDebugger = AutoDebugger(
            config.ENGINE, max_completion_tokens=100, stream=False
        )

        module_name = "main"

        while num_tries < 1:
            test_docker = synthesize_utils.test(
                    module_name=module_name, 
                    test=test, 
                    entry_point=entry_point
            )

            success, command, output = verifier.verify(
                program,
                test=test_docker,
                filename_program=f"{module_name}.py",
                filename_test="test.py",
            )

            utils.write_file(os.path.join(tmp_dir, f"{module_name}.py"), program)
            utils.write_file(os.path.join(tmp_dir, "test.py"), test_docker)
            if success:
                break
            else:
                logger.info(f"Try {num_tries}")
                prompt: ExplainerPrompt = ExplainerPrompt(
                    specification, program, "template.py", module_name=module_name, error=output
                )
                print(prompt)
                explanation = explainer.explain(prompt, temperature=0.0, max_tokens=100)
                print(explanation)

                debugger_prompt = DebuggerPrompt(
                    specification=specification,
                    program=program,
                    error=output,
                    explanation=explanation,
                    template_file="template_assertion_explain.py",
                    module_name=module_name
                )

                program = auto_debugger.debug(debugger_prompt, temperature=0.0)
                utils.write_file(os.path.join(tmp_dir, f"{module_name}-debugged.py"), program)

            num_tries += 1
        exit()
