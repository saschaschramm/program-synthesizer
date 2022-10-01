from logging import Logger

from components.auto_debugger.component import AutoDebugger
from components.verifier.component import Verifier
from components.verifier.component import VerificationError
import utils
import os.path
from logging_utils import get_logger
from config import config
from program import Program

logger: Logger = get_logger()


if __name__ == "__main__":
    SOURCE: str = os.path.join(config.DATA_DIR, "tasks-synthesized.json")
    utils.make_dir(config.TMP_EVAL_DIR)
    tasks = utils.read_file(SOURCE)
    auto_debugger: AutoDebugger = AutoDebugger()
    verifier: Verifier = Verifier(config.TMP_EVAL_DIR)

    for taskname, task in tasks.items():
        logger.info(f"{taskname} ---------------------------------")
        taskname: str = taskname.replace("/", "-")
        tmp_task_dir: str = os.path.join(config.TMP_EVAL_DIR, taskname)
        utils.make_dir(tmp_task_dir)
        utils.write_file(
            os.path.join(tmp_task_dir, f"{utils.filename(0)}.py"), task["program"]
        )
        utils.write_file(
            os.path.join(tmp_task_dir, f"{utils.filename(0)}-original.py"),
            task["prompt"],
        )

        program: str = task["program_2"]
        entry_point: str = task["entry_point"]
        num_tries: int = 0
        max_tries: int = 3
        while num_tries < max_tries:
            verifier_program = Program(program, timeout=3)
            verifier_program.add_test(task["test"], entry_point, assertion=False)
            try:
                path_executable: str = os.path.join(
                    taskname, f"{utils.filename(1)}-{num_tries}-exec.py"
                )
                command: str = verifier.verify(str(verifier_program), path_executable)
                logger.info(f"Verification succeeded – {command}")
                break
            except VerificationError as error:
                logger.error(f"{error}")
                logger.info(f"Try {num_tries}")
                program = auto_debugger.debug(
                    program, error, tmp_task_dir, f"{utils.filename(1)}-{num_tries}"
                )
            except Exception as exception:
                logger.error(f"Unexpected error: {exception}")
                exit()
            num_tries += 1
        task["program_3"] = program

    utils.write_json(os.path.join(config.TMP_EVAL_DIR, "tasks-debugged.json"), tasks)
