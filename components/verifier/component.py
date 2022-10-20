import subprocess
from tempfile import NamedTemporaryFile
from components.verifier.verification_error import VerificationError

class Verifier:
    def __init__(self) -> None:
        self.command_exec: str = "docker exec sandbox python /code/main.py"

    def verify(self, program: str) -> str:
        with NamedTemporaryFile(suffix='.py', delete=True) as tmp_file:
            tmp_file.write(program.encode())
            tmp_file.flush()
            command_copy: str = f"docker cp {tmp_file.name} sandbox:/code/main.py"
            command: str = f"{command_copy};{self.command_exec}"
            process: subprocess.Popen = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            stderr_str = stderr.decode("utf-8")
            stdout_str = stdout.decode("utf-8")
            #print(stderr_str)
            #print(stdout_str)
            lines: list[str] = stderr_str.splitlines()
            if len(lines) > 0:
                error_type: str = lines[-1]
                #if error_type == "AssertionError":
                #    assert_message: str = lines[-2].strip()
                #    message: str = f"{error_type}: {assert_message}"
                #else:
                message: str = error_type
                raise VerificationError(message)
            return command
