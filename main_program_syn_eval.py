from logging import Logger
import os
import utils
from config import config
from components.program_synthesizer.component import ProgramSynthesizer
from logging_utils import get_logger

logger: Logger = get_logger()


if __name__ == "__main__":
    tasks = utils.read_file(os.path.join(config.DATA_DIR, "tasks.json"))
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer(config.TMP_SYN_DIR)
    tasks_new = {}
    for taskname, task in tasks.items():
        if taskname != "HumanEval/5":
            continue

        taskname: str = taskname.replace("/", "-")
        tmp_task_dir: str = os.path.join(config.TMP_SYN_DIR, taskname)
        utils.make_dir(tmp_task_dir)
        program: str = task["program"].strip()
        utils.write_file(os.path.join(tmp_task_dir, "0000.py"), program)

        for index, specification in enumerate([task["specification"]]):
            filename: str = utils.filename(index+1)
            logger.info(f"{taskname} – {filename} ---------------------------------")
            logger.info(f"Specification: {specification}")
            program: str = program_synthesizer.synthesize(
                specification, program, os.path.join(taskname, filename)
            )
        tasks_new[taskname] = task.copy()
        tasks_new[taskname]["program_2"] = program
    utils.write_json(
        os.path.join(config.TMP_SYN_DIR, "tasks-synthesized.json"), tasks_new
    )
