class Speed:
    __slots__ = ('kmph',)

    def __init__(self):
        self.kmph = 0

    @property
    def meters_sec(self):
        return self.kmph / 3.6

    @meters_sec.setter
    def meters_sec(self, value):
        self.kmph = value * 3.6

    @property
    def mph(self):
        return self.kmph / 1.609

    @mph.setter
    def mph(self, value):
        self.kmph = value * 1.609


if __name__ == '__main__':
    speed = Speed()
    speed.kmph = 100
    print(1)
