class VerificationError(Exception):
    def __init__(self, exception: Exception) -> None:
        super().__init__(exception)
        self.name: str = exception.__class__.__name__
        if len(exception.args) > 0:
            self.message: str = exception.args[0]
