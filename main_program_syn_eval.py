from logging import Logger
import os
import utils
from config import config
from components.program_synthesizer.component import ProgramSynthesizer
from components.program_synthesizer.completion_prompt import (
    CompletionPrompt as ProgramPrompt,
)
from components.test_synthesizer.component import TestSynthesizer
from components.test_synthesizer.completion_prompt import CompletionPrompt as TestPrompt

from logging_utils import get_logger

logger: Logger = get_logger()

if __name__ == "__main__":
    utils.make_dir(config.TMP_SYN_DIR)
    tasks = utils.read_file(os.path.join(config.DATA_DIR, "tasks.json"))
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer(
        config.ENGINE, max_completion_tokens=500, stream=False
    )
    test_synthesizer = TestSynthesizer(
        config.ENGINE, max_completion_tokens=500, stream=False
    )

    tasks_new = {}
    for taskname, task in tasks.items():
        # if taskname != "HumanEval/161":
        #    continue

        taskname: str = taskname.replace("/", "-")
        filename: str = utils.filename(0)
        tmp_dir: str = os.path.join(config.TMP_SYN_DIR, taskname, filename)
        program_old: str = task["program"].strip()
        utils.make_dir(tmp_dir)
        utils.write_files(tmp_dir, [(f"main.py", program_old)])


        specification: str = task["specification"]
        filename: str = utils.filename(1)
        logger.info(f"{taskname} – {filename} ---------------------------------")
        logger.info(f"Specification: {specification}")

        program_prompt: ProgramPrompt = ProgramPrompt(
            specification, program_old, template_file="template.py"
        )

        program_new = program_synthesizer.synthesize(program_prompt, temperature=0.0)
        test_prompt = TestPrompt(
            specification=specification,
            program_old=program_old,
            program_new=program_new,
            template_file="template.py",
        )
        test: str = test_synthesizer.synthesize(test_prompt, temperature=0.0)
        tmp_dir: str = os.path.join(config.TMP_SYN_DIR, taskname, filename)
        utils.make_dir(tmp_dir)
        utils.write_files(tmp_dir, [
            (f"test.py", test), 
            (f"main.prompt", str(program_prompt)),
            (f"test.prompt", str(test_prompt)),
            (f"main.py", program_new),])

        tasks_new[taskname] = task.copy()
        tasks_new[taskname]["program_synthesized"] = program_new
        tasks_new[taskname]["test_synthesized"] = test

    utils.write_json(os.path.join(config.TMP_DIR, "tasks-synthesized.json"), tasks_new)
