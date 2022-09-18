import os
from typing import Any
from verification_error import VerificationError
import builtins

class Verifier():

    def __init__(self, globals) -> None:
        self._globals: dict[str, Any] = globals

    def verify(self, code: str) -> None:
        try:
            #os.popen(f"python -c '{code}'")
            builtins.exec(code, self._globals, {})
        except Exception as exception:
            # https://docs.python.org/3/library/exceptions.html
            # The Python interpreter can generate Built-in Exceptions
            raise VerificationError(exception)