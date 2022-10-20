import utils

TIMEOUT: str = """import signal
def handle_timeout(sig, frame):
    raise TimeoutError(f"Program timed out after {timeout} seconds")
signal.signal(signal.SIGALRM, handle_timeout)
signal.alarm({timeout})"""

TEST_TEMPLATE: str = """{program}\n\n{test}\n\n{timeout}\n\ncheck({entry_point})"""
TEST_TEMPLATE2: str = """{program}\n\n{timeout}\n\n{test}"""


class Program:
    def __init__(self, program: str, timeout: int) -> None:
        self.program: str = program.strip()
        self.timeout: str = TIMEOUT.format(timeout=timeout)

    def write(self, path: str):
        utils.write_file(path, self.program)

    def add_tests(self, test: str, entry_point: str) -> None:
        self.program = TEST_TEMPLATE.format(
            program=self.program,
            test=test.strip(),
            timeout=self.timeout,
            entry_point=entry_point,
        )

    def add_syn_tests(self, test: str, entry_point: str) -> None:
        self.program = TEST_TEMPLATE2.format(
            program=self.program,
            test=test.strip(),
            timeout=self.timeout,
            entry_point=entry_point,
        )

    def add_comment_before(self, spec: str):
        self.program = f'"""{spec}\n"""\n{self.program}'

    def add_comment_after(self, test: str):
        self.program = f'{self.program}\n"""{test}\n"""'

    def __str__(self) -> str:
        return self.program
