from enum import Enum
from enum import auto as enum_auto

class _surpression_statuses(Enum):
    InEnter = enum_auto()
    OnYield = enum_auto()
    HandlingException = enum_auto()

class SuppressErrors:
    def __init__(self, *exceptions):
        self._exc: tuple = exceptions
        self._status: _surpression_statuses = _surpression_statuses.OnYield

    def close(self):
        self.__exit__(None, None, None)

    def __enter__(self):
        if self._status == _surpression_statuses.OnYield:
            pass
        else:
            raise SyntaxWarning("There already is an open instance of SurpressErrors()!")
        self.close()
        self._status = _surpression_statuses.InEnter

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._status = _surpression_statuses.HandlingException
        try:
            if self._exc == ():
                return True
            if exc_type is None:
                return True
            for exc in self._exc:
                if isinstance(exc_val, exc) or exc_type == exc:
                    pass
                else:
                    break
            else:
                return True
            return False
        finally:
            self._status = _surpression_statuses.OnYield