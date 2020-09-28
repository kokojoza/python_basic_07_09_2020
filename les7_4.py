from abc import ABC, abstractmethod


class SomeInterface(ABC):

    @abstractmethod
    def get_name(self, a: int, b: str) -> int:
        pass

    @abstractmethod
    def get_idx(self):
        pass


class Some(SomeInterface):
    def __init__(self, name):
        """
        :param name:
        """
        self.name = name
        self.idx = 0

    def get_idx(self):
        return self.idx

    def get_name(self):
        return self.name


if __name__ == '__main__':
    some = Some('NAME')
