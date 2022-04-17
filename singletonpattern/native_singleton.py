class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
            print(cls._instances)
        return cls._instances[cls]


class DBConnector(metaclass=SingletonMeta):
    def __init__(self, host, port):
        self.db = f"dummy connection to db://{host}:{port}"


class Settings(metaclass=SingletonMeta):
    def __init__(self, path):
        self.settings = self._read_file(path)

    @staticmethod
    def _read_file(path: str) -> dict:
        return {'path': path}
