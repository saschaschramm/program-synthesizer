from components.verifier.component import Verifier
import utils

verifier: Verifier = Verifier()
program: str = utils.read_file("demos/demo2/main.py")
test: str = utils.read_file("demos/demo2/test.py")
_, command, error = verifier.verify(program=program, test=test, filename_program="main.py", filename_test="test.py")
print(error)

