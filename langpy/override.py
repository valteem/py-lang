class Base():
    def __init__(self) -> None:
        self._param1 = 1
        self._param2 = "Base"
    def show(self) -> (int, str):
        return self._param1, self._param2
    def add(self) -> int:
        return self._param1 + len(self._param2)
    
class Heir(Base):
    def __init__(self, arg1: int, arg2: str) -> None:
        self._param1 = arg1
        self._param2 = arg2
    def show(self) -> str:
        return str(self._param1) + ' ' + self._param2