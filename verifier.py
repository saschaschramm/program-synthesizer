import builtins
from typing import Any
from verification_error import VerificationError

class Verifier():

    def __init__(self, globals: dict[str, Any], locals: dict[str, Any]) -> None:
        self._globals: dict[str, Any] = globals
        self._locals: dict[str, Any] = locals

    def verify(self, path: str) -> None:
        try:
            self._execute(path)
        except NameError as e:
            raise VerificationError(e, spec="Fix imports and move main to the end of the file")
        except TypeError as e:
            raise VerificationError(e, spec="Convert bytes to str")
        except UnicodeDecodeError as e:
            raise VerificationError(e, spec="Use correct encoding")        
        except Exception as e:
            print(e)
            raise Exception("Unexpected error")

    def _execute(self, path: str) -> None:
        with open(path, mode="r", encoding="utf-8") as file:
            code: str = file.read()
            builtins.exec(code, self._globals, self._locals)