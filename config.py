import os

class Base:
    pass

class Config(Base):
    DATA_DIR: str = "data"
    TMP_DIR: str = "tmp"
    TMP_EVAL_DIR: str = os.path.join("tmp", "eval")
    TMP_SYN_DIR: str = os.path.join("tmp", "syn")
    #SPEC_FILE: str = os.path.join("specs", "program-oidc.spec")
    SPEC_FILE: str = os.path.join("specs", "program-hello.spec")
    NUM_TOKENS: int = 1500
    EVALUATION: bool = False

config: Config = Config()