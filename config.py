import os


class Base:
    pass


class Config(Base):
    DATA_DIR: str = "data"
    TMP_DIR: str = "tmp"
    TMP_EVAL_DIR: str = os.path.join("tmp", "eval")
    TMP_SYN_DIR: str = os.path.join("tmp", "syn")
    TMP_DEBUG_DIR: str = os.path.join("tmp", "debug")

    # SPEC_FILE: str = os.path.join("specs", "program-oidc.spec")
    # SPEC_FILE: str = os.path.join("specs", "program-bug.spec")
    SPEC_FILE: str = os.path.join("specs", "program-hello.spec")
    NUM_TOKENS: int = 500
    EVALUATION: bool = False


config: Config = Config()
