class MixinLang:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_lang):
        self._language = new_lang

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class KeyBoard(MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__()
        self.name = name
        self.price = price
        self.warranty = quantity

    def __str__(self):
        return self.name