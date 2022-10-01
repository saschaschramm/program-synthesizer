from logging import Logger
import os
import utils
from config import config
from components.auto_debugger.component import AutoDebugger
from components.program_synthesizer.component import ProgramSynthesizer
from components.verifier.component import Verifier
from components.verifier.verification_error import VerificationError
from logging_utils import get_logger

logger: Logger = get_logger()


def _specifications(filename: str) -> list[str]:
    lines = []
    with open(filename, mode="r", encoding="utf-8") as file:
        lines += file.readlines()
        # Ignore empty lines
        lines = [line for line in lines if line.strip() != ""]
        # Ignore comments
        lines = [line for line in lines if not line.startswith("#")]
        return [line.strip() for line in lines]


def main() -> None:
    utils.make_dir(config.TMP_SYN_DIR)
    verifier: Verifier = Verifier(config.TMP_SYN_DIR)
    auto_debugger: AutoDebugger = AutoDebugger()
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer(config.TMP_SYN_DIR)
    program: str = utils.read_file(os.path.join(config.DATA_DIR, "main.py"))
    utils.write_file(os.path.join(config.TMP_SYN_DIR, "0000.py"), program.strip())
    specifications: list[str] = _specifications(config.SPEC_FILE)

    for index, specification in enumerate(specifications):
        filename: str = utils.filename(index + 1)
        logger.info(f"{filename} ---------------------------------")
        logger.info(f"Specification: {specification}")
        program: str = program_synthesizer.synthesize(specification, program, filename)
        num_tries: int = 0
        max_tries: int = 3
        while num_tries < max_tries:
            try:
                verifier.verify(program, None)
                logger.info(f"Verification succeeded")
                break
            except VerificationError as error:
                logger.error(f"{error}")
                logger.info(f"Try {num_tries}")
                program = auto_debugger.debug(program, error, filename, num_tries)
            except Exception as exception:
                print(exception)
                exit()
            num_tries += 1


if __name__ == "__main__":
    main()
