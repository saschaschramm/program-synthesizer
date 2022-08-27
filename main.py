import os
import shutil
from verification_error import VerificationError
import utils
from config import config
from verifier import Verifier
from code_synthesizer import CodeSynthesizer
from logging_utils import get_logger
from logging import Logger


logger: Logger = get_logger()

def _initalize() -> None:
    if not config.DEBUG:
        program: str = utils.read_file("example", "main", "py")
        utils.write_file(program.strip(), "program", "main", "py")

def _clean() -> None:
    if not config.DEBUG:
        if os.path.exists(config.PROGRAM_DIR):
            shutil.rmtree(config.PROGRAM_DIR)
        os.makedirs(config.PROGRAM_DIR)

    if os.path.exists(config.TMP_DIR):
        shutil.rmtree(config.TMP_DIR)
    os.makedirs(config.TMP_DIR)

def _specifications(filename: str) -> list[str]:
    lines = ["Initial commit"]
    with open(filename, mode="r", encoding="utf-8") as file:
        lines += file.readlines()
        # Ignore empty lines
        lines = [line for line in lines if line.strip() != ""]
        # Ignore comments
        lines = [line for line in lines if not line.startswith("#")]
        return [line.strip() for line in lines]


def main(verifier: Verifier, program_spec) -> None:
    _clean()
    _initalize()
    old_name: str = "old"
    new_name: str = "new"
    specifications: list[str] = _specifications(program_spec)
    code_synthesizer: CodeSynthesizer = CodeSynthesizer()
    program_path: str = os.path.join(config.PROGRAM_DIR, "main.py")
    for index, specification in enumerate(specifications):
        filename_spec = f"{index*10:04d}"
        logger.info(f"{filename_spec} ---------------------------------")
        logger.info(f"Specification: {specification}")
        code_synthesizer.synthesize(specification, old_name, new_name, filename_spec)
        num_tries: int = 0
        max_tries: int = 3
        while num_tries < max_tries:
            try:
                verifier.verify(program_path)
                logger.info(f"Verification succeeded")
                break
            except VerificationError as e:
                logger.error(f"Verification failed: {e.error_name}")
                logger.error(f"Specification {e.error_name} - try {num_tries}: {e.spec}")
                code_synthesizer.synthesize(e.spec, old_name, new_name, 
                                            f"{filename_spec}-{num_tries}-{e.error_name.lower()}-fix")
            except Exception as e:
                print(e)
                exit()
            num_tries += 1

if __name__ == "__main__":
    verifier: Verifier = Verifier(globals(), locals())
    main(verifier, os.path.join("specs", "program-toy.spec"))