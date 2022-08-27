class Base:
    pass

class Config(Base):
    DEBUG = False
    SPECIFICATIONS_DIR: str = "specifications"
    PROGRAM_DIR: str = "program"
    TMP_DIR: str = "tmp"

config: Config = Config()