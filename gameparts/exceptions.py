class FieldIndexError(IndexError):
    """"Данный класс преназначает сообщение об ошибке,
    при некорректном вводе координат.
    """

    def __str__(self):
        return 'Введено значение за границами игрового поля'


class CellOcupiedError(Exception):
    def __str__(self):
        return 'Ячейка занята, попробуйте ввести другие координаты'
