from threading import Lock


class SingletonMeta(type):
    __lock = Lock()
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


# Uncomment line below to apply singleton for all class in this file
# __metaclass__ = SingletonMeta

class DBConnector(metaclass=SingletonMeta):
    def __init__(self, host, port):
        self.db = f"dummy connection to db://{host}:{port}"


class Settings(metaclass=SingletonMeta):
    def __init__(self, path):
        self.settings = self._read_file(path)

    @staticmethod
    def _read_file(path: str) -> dict:
        return {'path': path}
