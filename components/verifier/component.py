import os
import subprocess
from typing import Optional
from components.verifier.verification_error import VerificationError
import utils


class Verifier:
    def __init__(self, path) -> None:
        self.path: str = path
        self.program_path = os.path.join(self.path, "main.py")
        self.command_copy: str = f"docker cp {self.program_path} sandbox:/code/main.py"
        self.command_exec: str = "docker exec sandbox python /code/main.py"

    def verify(self, program: str, path_executable: Optional[str]) -> str:
        utils.write_file(self.program_path, program)
        command: str = f"{self.command_copy};{self.command_exec}"
        process: subprocess.Popen = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        stderr_str = stderr.decode("utf-8")

        lines = stderr_str.splitlines()

        if path_executable is not None:
            utils.write_file(os.path.join(self.path, path_executable), program)

        if len(lines) > 0:
            message = lines[-1]
            raise VerificationError(message)
        return command
