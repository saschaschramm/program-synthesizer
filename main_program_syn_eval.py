from logging import Logger
import os
import utils
from config import config
from components.program_synthesizer.component import ProgramSynthesizer
from components.program_synthesizer.completion_prompt import CompletionPrompt
from logging_utils import get_logger

logger: Logger = get_logger()

if __name__ == "__main__":
    utils.make_dir(config.TMP_SYN_DIR)
    tasks = utils.read_file(os.path.join(config.DATA_DIR, "tasks.json"))
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer()
    tasks_new = {}
    for taskname, task in tasks.items():
        # if taskname != "HumanEval/161":
        #    continue

        taskname: str = taskname.replace("/", "-")
        # Create tmp task dir
        tmp_task_dir: str = os.path.join(config.TMP_SYN_DIR, taskname)
        utils.make_dir(tmp_task_dir)

        # Save initial program
        program: str = task["program"].strip()
        utils.write_file(os.path.join(tmp_task_dir, "0000.py"), program)

        specification: str = task["specification"]
        filename: str = utils.filename(1)
        logger.info(f"{taskname} – {filename} ---------------------------------")
        logger.info(f"Specification: {specification}")

        prompt: CompletionPrompt = CompletionPrompt(
            specification, program, template_file="template_test.py"
        )
        program, tests = program_synthesizer.synthesize(prompt, temperature=0.0)
        utils.write_file(os.path.join(tmp_task_dir, f"{filename}.test"), tests)
        utils.write_file(os.path.join(tmp_task_dir, f"{filename}.prompt"), str(prompt))
        utils.write_file(os.path.join(tmp_task_dir, f"{filename}.py"), program)
        tasks_new[taskname] = task.copy()
        tasks_new[taskname]["program_synthesized"] = program
        tasks_new[taskname]["test_synthesized"] = tests

    utils.write_json(os.path.join(config.TMP_DIR, "tasks-synthesized.json"), tasks_new)
