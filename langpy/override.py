# typing.override decorator introduced since Python 3.12
# typing_extensions provide backward compatibility for Python >= 3.9
from typing import Union
from typing_extensions import override

class Base():
    def __init__(self, arg: Union[int, str]) -> None:
        self.param: Union[int, str] = arg
    def show(self) -> Union[int, str]:
        return self.param
    
class Heir(Base):
    @override
    def show(self) -> str:
        return str(self.param)