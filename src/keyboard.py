from src.item import Item


class MixinLang:
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class KeyBoard(Item, MixinLang):
    pass
