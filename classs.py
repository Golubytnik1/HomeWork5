# 27.12.2022

class Hero:

    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti

    def vizov(self):
        print(f'Имя героя: {self.name}\n'
              f'Способность: {self.abyliti}')


class Hero_super(Hero):

    def __init__(self, name, abyliti):
        super().__init__(name, abyliti)

    def nick(self):
        print(f'Имя героя: {self.name}')

    def __str__(self):
        return f'Способность: {self.abyliti}'

    def phrase(self):
        print('it is super_hero')