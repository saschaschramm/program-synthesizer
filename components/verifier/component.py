import subprocess
from components.verifier.verification_error import VerificationError

class Verifier():

    def __init__(self, timeout:int = 3) -> None:
        self._timeout: int = timeout

    def verify(self, path: str) -> None:
        cmd: str = f"python {path}"
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(timeout=self._timeout)
            stderr_str = stderr.decode("utf-8")
            # https://docs.python.org/3/library/exceptions.html
            # The Python interpreter can generate Built-in Exceptions
            lines = stderr_str.splitlines()
            if len(lines) > 0:
                message = lines[-1]
                raise VerificationError(message)

        except subprocess.TimeoutExpired as error:
            raise VerificationError(f"TimeoutExpired: {error}")
  