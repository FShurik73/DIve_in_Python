class Archive:

    '''
    Класс создает объекты которые содержат число и строку, а так же содержат в себе архив
    всех предыдущих созданных объектов.
    Keyword arguments:
    number - числа
    letter - строка
    arch - архив
    '''

    _instance = []

    def __new__(cls, number: int, letter: str):
        instance = super().__new__(cls)
        instance.number = number
        instance.letter = letter
        instance.arch = cls._instance.copy()
        cls._instance.append(instance)
        return instance

    def __str__(self):
        return f'{self.number} {self.letter} | {self.arch}' 

    def __repr__(self):
        return f'{self.number} {self.letter}'

a = Archive(1, 'a')
print(a)
b = Archive(2, 'b')
print(b)
c = Archive(3, 'c')
print(c)
d = Archive(4, 'd')
print(d)













