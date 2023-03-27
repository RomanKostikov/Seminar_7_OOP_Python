class Animal:
    def __init__(self, nickname):
        self._nickname = nickname

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, new_nickname):
        self._nickname = new_nickname

    def __str__(self):
        return self.nickname