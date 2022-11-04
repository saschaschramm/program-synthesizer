from typing import Optional
import re

ASSERTION_ERROR: str = "AssertionError"

TIMEOUT: str = """import signal
def handle_timeout(sig, frame):
    raise TimeoutError(f"Program timed out after {timeout} seconds")
signal.signal(signal.SIGALRM, handle_timeout)
signal.alarm({timeout})"""


def test(module_name: str, test: str, entry_point: Optional[str]) -> str:
    timeout_str: str = TIMEOUT.format(timeout=3)
    if entry_point is None:
        template = """from {module_name} import *\n\n{timeout}\n\n{test}"""
        return template.format(
            module_name=module_name,
            test=test,
            timeout=timeout_str,
        )
    else:
        template = """from {module_name} import *\n\n{test}\n\n{timeout}\n\ncheck({entry_point})"""
        return template.format(
            module_name=module_name,
            test=test,
            timeout=timeout_str,
            entry_point=entry_point,
        )


def remove_line_number(text: str) -> str:
    tmp: str = re.sub(r", line \d+,", "", text)
    return re.sub(r", line \d+", "", tmp)


def last_line(output: str) -> str:
    lines: list[str] = output.splitlines()
    return lines[-1]


def debugger_params(string: str) -> tuple[str, float]:
    if ASSERTION_ERROR in string:
        template_file = "template_assertion.py"
        temperature = 0.7
    else:
        template_file = "template_interpreter.py"
        temperature = 0.0
    return template_file, temperature
