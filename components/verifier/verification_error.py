class VerificationError(Exception):
    def __init__(self, message: str) -> None:
        self.name: str = "VerificationError"
        self.sub_name: str 
        self.message: str = message
