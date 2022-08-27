class VerificationError(Exception):
    def __init__(self, exception: Exception, spec: str) -> None:      
        super().__init__(exception)
        self.spec: str = spec
        self.error_name: str = exception.__class__.__name__