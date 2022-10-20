from collections import Counter
from logging import Logger
from components.verifier.component import Verifier
from components.verifier.component import VerificationError
import utils
from logging_utils import get_logger
from config import config
import pandas as pd
import os
from program import Program


logger: Logger = get_logger()

def _list_to_html(list: list[str]) -> None:
    df: pd.DataFrame = pd.DataFrame({"Error Type": Counter(list).keys(), "Count": Counter(list).values()})
    df = df.sort_values(by="Count", ascending=False)
    html = df.to_html(index=False)
    utils.write_file(os.path.join(config.TMP_EVAL_DIR, "tmp.md"), html)

if __name__ == "__main__":
    SOURCE: str = config.TMP_DIR
    TARGET: str = config.TMP_EVAL_DIR
    EVAL_AFTER_DEBUG = True
    
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
        program_verified: Program = Program(task[OPTION[0]], timeout=3)
        program_verified.add_tests(task["test"], entry_point)


        program_log: Program = Program(task[OPTION[0]], timeout=3)
        program_log.add_tests(task["test"], entry_point)
        program_log.add_comment_before(task["specification"])
        program_log.add_comment_after(task["test_synthesized"])
        canonical_solution: str = task["canonical_solution"]
        program_log.add_comment_after(f"{entry_point}{canonical_solution}")
        taskname: str = taskname.replace("/", "-")

        try:
            command = verifier.verify(str(program_verified))
            logger.info(f"Verification succeeded – {command}")
            num_pass += 1
            utils.write_file(os.path.join(TARGET, f"{taskname}-success.py"), str(program_log))
        except VerificationError as error:
            logger.error(f"{error}")
            error = str(error)
            if ":" in error:
                error_types.append(error.split(":")[0])
            else:
                error_types.append(error)
            utils.write_file(os.path.join(TARGET, f"{taskname}-fail.py"), str(program_log))
        except Exception as exception:
            logger.error(f"Unexpected error: {exception}")
            exit()

    pass_rate: float = num_pass / len(tasks)
    print("num_pass", num_pass)
    print(f"pass_rate {pass_rate*100:.2f}%")
    _list_to_html(error_types)