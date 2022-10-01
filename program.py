import utils

TIMEOUT: str = """import signal
def handle_timeout(sig, frame):
    raise TimeoutError(f"Program timed out after {timeout} seconds")
signal.signal(signal.SIGALRM, handle_timeout)
signal.alarm({timeout})"""

TEST_TEMPLATE: str = """{program}\n\n{test}\n\n{timeout}\n\ncheck({entry_point})"""


class Program:
    def __init__(self, program: str, timeout: int) -> None:
        self.program: str = program.strip()
        self.timeout: int = TIMEOUT.format(timeout=timeout)

    def write(self, path: str):
        utils.write_file(path, self.program)

    def add_test(self, test: str, entry_point: str, assertion: bool) -> str:
        if not assertion:
            test = test.replace("assert ", "")
        #self.program = f"""{self.program}\n\n{test.strip()}\n\n{self.timeout}\n\ncheck({entry_point})"""
        self.program = TEST_TEMPLATE.format(program=self.program, test=test.strip(), timeout=self.timeout, entry_point=entry_point)

    def __str__(self) -> str:
        return self.program


if __name__ == "__main__":
    program = Program("abc", 3)
    program.add_test("test", "entry_point")
    print(str(program))
