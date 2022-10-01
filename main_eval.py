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


def _list_to_html(list: list[str]) -> str:
    print(Counter(list))
    df: pd.DataFrame = pd.DataFrame({"Error Type": Counter(list).keys(), "Count": Counter(list).values()})
    df = df.sort_values(by="Count", ascending=False)
    html = df.to_html(index=False)
    utils.write_file(os.path.join(config.TMP_EVAL_DIR, "tmp.md"), html)

if __name__ == "__main__":
    SOURCE: str = os.path.join(config.DATA_DIR, "tasks-debugged-no-error.json")
    tasks = utils.read_file(SOURCE)
    utils.make_dir(config.TMP_EVAL_DIR)
    verifier: Verifier = Verifier(config.TMP_EVAL_DIR)
    error_types: list[str] = []
    num_pass: int = 0
    for taskname, task in tasks.items():
        logger.info(f"{taskname} ---------------------------------")     
        program: str = task["program_3"]
        entry_point: str = task["entry_point"]
        try:
            verifier_program = Program(program, timeout=3)
            verifier_program.add_test(task["test"], entry_point, assertion=True)
            command = verifier.verify(str(verifier_program), None)
            logger.info(f"Verification succeeded – {command}")
            num_pass += 1
        except VerificationError as error:
            logger.error(f"{error}")
            error = str(error)
            if ":" in error:
                error_types.append(error.split(":")[0])
            else:
                error_types.append(error)  
        except Exception as exception:
            logger.error(f"Unexpected error: {exception}")
            exit()

    pass_rate: float = num_pass / len(tasks)
    print("num_pass", num_pass)
    print(f"pass_rate {pass_rate*100:.2f}%")
    _list_to_html(error_types)
