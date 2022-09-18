import os

class Base:
    pass

class Config(Base):
    DEBUG = False
    PROGRAM_DIR: str = "program"
    TMP_DIR: str = "tmp"
    #SPEC_FILE: str = os.path.join("specs", "program-oidc.spec")
    SPEC_FILE: str = os.path.join("specs", "program-hello.spec")

config: Config = Config()