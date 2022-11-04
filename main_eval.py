from logging import Logger
from components.verifier.component import Verifier
import utils
import synthesize_utils
from logging_utils import get_logger
from config import config
import os


logger: Logger = get_logger()

SOURCE: str = config.TMP_DIR
TARGET: str = config.TMP_EVAL_DIR
EVAL_AFTER_DEBUG: bool = True

if __name__ == "__main__":

    if EVAL_AFTER_DEBUG:
        OPTION = ("program_debugged", "tasks-debugged.json")
    else:
        OPTION = ("program_synthesized", "tasks-synthesized.json")

    tasks: dict = utils.read_file(os.path.join(SOURCE, OPTION[1]))
    utils.make_dir(TARGET)
    verifier: Verifier = Verifier()
    error_types: list[str] = []
    num_pass: int = 0
    for taskname, task in tasks.items():
        logger.info(f"{taskname} ---------------------------------")
        entry_point: str = task["entry_point"]
        initial_program: str = task["program"]
        program: str = task[OPTION[0]]
        test: str = task["test"]
        specification: str = task["specification"]
        canonical_solution: str = task["canonical_solution"]
        module_name: str = "main"

        test: str = synthesize_utils.test(
            module_name=module_name, test=test, entry_point=entry_point
        )
        taskname: str = taskname.replace("/", "-")
        success, command, output = verifier.verify(
            program,
            test=test,
            filename_program=f"{module_name}.py",
            filename_test="test.py",
        )
        flag: str = ""
        if success:
            num_pass += 1
            logger.info(f"Verification succeeded")
            flag = "success"
        else:
            logger.error(f"{output}")
            flag = "fail"

        tmp_dir: str = os.path.join(TARGET, f"{taskname}_{flag}")
        utils.make_dir(tmp_dir)
        utils.write_files(tmp_dir, [
            ("test.py", test), 
            ("specification.txt", specification),
            ("canonical_solution.py", f"{initial_program}\n{canonical_solution}"),
            ("main.py", program),]
            )

    pass_rate: float = num_pass / len(tasks)
    print("num_pass", num_pass)
    print(f"pass_rate {pass_rate*100:.2f}%")
