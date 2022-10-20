import openai
from openai.error import RateLimitError
import time
from typing import Any
import logging

logger = logging.getLogger("openai")
logger.disabled = True


class Completion:

    @classmethod
    def create(cls, prompt: str, temperature: float, max_completion_tokens: int, stop: list[str], engine: str) -> dict:
        max_num_tries = 3
        kwargs: dict[str, Any] = {
            "temperature": temperature,
            "prompt": prompt,
            "max_tokens": max_completion_tokens,
            "stop": stop,
        }
        kwargs["engine"] = engine
        num_tries: int = 0
        while num_tries < max_num_tries:
            try:
                completion: Any = openai.Completion.create(**kwargs)
                if isinstance(completion, dict):
                    return completion
                else:
                    raise NotImplementedError
            except RateLimitError as error:
                print(f"RateLimitError {num_tries+1}/{max_num_tries}")
                num_tries += 1
                time.sleep(30)
        raise Exception(f"Failed to create completion after {num_tries} tries")
