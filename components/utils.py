from typing import Any

def _completion_text(completion) -> Any:
    for element in completion:
        yield element["choices"][0]["text"]

def completion_text(completion: Any, stream: bool) -> Any:
    if stream is True:
        return _completion_text(completion)
    else:
        return completion["choices"][0]["text"]