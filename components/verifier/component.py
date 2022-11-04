import subprocess
from tempfile import NamedTemporaryFile


class Verifier:
    def _execute(self, command: str) -> tuple[str, str]:
        process: subprocess.Popen = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        stdout_str: str = stdout.decode("utf-8")
        stderr_str: str = stderr.decode("utf-8")
        return stdout_str, stderr_str

    def verify(
        self, program: str, test: str, filename_program: str, filename_test: str
    ):
        with NamedTemporaryFile(suffix=".py", delete=True) as tmp_file:
            tmp_file.write(program.encode())
            tmp_file.flush()
            command: str = f"docker cp {tmp_file.name} sandbox:/app/{filename_program}"
            self._execute(command)


        with NamedTemporaryFile(suffix=".py", delete=True) as tmp_file:
            tmp_file.write(test.encode())
            tmp_file.flush()
            command: str = f"docker cp {tmp_file.name} sandbox:/app/{filename_test}"
            self._execute(command)

        command: str = f"docker exec sandbox python {filename_test}"
        stdout_str, stderr_str = self._execute(command)
        if len(stderr_str.strip()) > 0:
            return False, command, stderr_str.strip()
        else:
            return True, command, stdout_str.strip()
