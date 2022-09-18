import os
from auto_debugger.component import AutoDebugger
from verification_error import VerificationError
from verifier import Verifier
import utils

if __name__ == "__main__":
    auto_debugger = AutoDebugger()
    verifier: Verifier = Verifier(globals())
    for filename in ["code1", "code2"]:
        path = os.path.join("auto_debugger", "data")
        code = utils.read_file(path, filename, "py")
        try:
            verifier.verify(code)
        except VerificationError as error:
            prompt, code = auto_debugger.debug(code, error)
            print(error)