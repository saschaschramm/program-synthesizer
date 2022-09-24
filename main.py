from logging import Logger
from os.path import join
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


def _verify(verifier, auto_debugger: AutoDebugger, filename, tmp_dir, program):
    num_tries: int = 0
    max_tries: int = 3
    while num_tries < max_tries:
        try:
            verifier.verify(join(tmp_dir, "main.py"))
            logger.info(f"Verification succeeded")
            break
        except VerificationError as error:
            logger.error(f"{error}")
            logger.info(f"Try {num_tries}")
            prompt, program = auto_debugger.debug(program, error)
            filename_fix = f"{filename}-{num_tries}-{error.name.lower()}-fix"
            utils.persist(str(prompt), program, tmp_dir, filename_fix)
        except Exception as exception:
            print(exception)
            exit()
        num_tries += 1


def _synthesize(program_synthesizer, verifier, auto_debugger, specifications, taskname):
    if taskname is None:
        tmp_dir = config.TMP_DIR
    else:
        tmp_dir = join(config.TMP_DIR, taskname)

    for index, specification in enumerate(specifications):
        filename = f"{(index+1)*10:04d}"
        logger.info(f"{taskname} – {filename} ---------------------------------")
        logger.info(f"Specification: {specification}")
        old_program: str = utils.read_file(tmp_dir, "main", "py").strip()
        prompt, program = program_synthesizer.synthesize(specification, old_program)
        utils.persist(str(prompt), program, tmp_dir, filename)
        if verifier is not None:
            _verify(verifier, auto_debugger, filename, tmp_dir, program)


def main() -> None:
    utils.make_dir(config.TMP_DIR)
    program_synthesizer: ProgramSynthesizer = ProgramSynthesizer()
    if config.EVALUATION:
        tasks = utils.read_file("data", "tasks", "json")
        for taskname, task in tasks.items():
            taskname = taskname.replace("/", "-")
            utils.make_dir(join(config.TMP_DIR, taskname))
            specifications = [task["specification"]]
            initial_program = task["program"]
            utils.initalize(join(config.TMP_DIR, taskname), initial_program)
            _synthesize(program_synthesizer, None, None, specifications, taskname)
    else:
        verifier: Verifier = Verifier()
        auto_debugger: AutoDebugger = AutoDebugger()
        initial_program = utils.read_file(config.DATA_DIR, "main", "py")
        utils.initalize(config.TMP_DIR, initial_program)
        specifications = _specifications(config.SPEC_FILE)
        _synthesize(program_synthesizer, verifier, auto_debugger, specifications, None)


if __name__ == "__main__":
    main()
