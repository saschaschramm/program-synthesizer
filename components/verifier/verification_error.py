class VerificationError(Exception):
    def __init__(self, message: str) -> None:
        self.name: str = "VerificationError"
        self.message: str = message
