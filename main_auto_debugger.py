import os
from components.auto_debugger.component import AutoDebugger
from components.verifier.component import Verifier
from components.verifier.verification_error import VerificationError
from config import config
import utils


def test_1() -> None:
    auto_debugger = AutoDebugger()
    verifier: Verifier = Verifier()
    for filename in ["program_1.py", "program_2.py"]:
        program_path: str = os.path.join(config.DATA_DIR, "auto_debugger", filename)
        try:
            verifier.verify(program_path)
            print(f"--- OK {filename}")
        except VerificationError as error:
            program = utils.read_file_with_path(program_path)
            prompt, program = auto_debugger.debug(program, error)
            print(f"--- ERROR {filename}")
            print(error)
            print("--- PROGRAM")
            print(program)

def test_2() -> None:
    auto_debugger = AutoDebugger()
    verifier: Verifier = Verifier()
    filename = "foo.py"
    program_path: str = filename
    try:
        verifier.verify(program_path)
        print(f"--- OK {filename}")
    except VerificationError as error:
        program = utils.read_file_with_path(program_path)
        prompt, program = auto_debugger.debug(program, error)
        print(f"--- ERROR {filename}")
        print(error)
        print("--- PROGRAM")
        print(program)

if __name__ == "__main__":
    #test_1()
    test_2()
