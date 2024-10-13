from .exceptions import FieldIndexError, CellOcupiedError


class Board:
    """Этот класс описывает игровое поле для 'крестиков-ноликов'."""

    field_size: int = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(
                self.field_size
            )
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 9)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )

    def is_board_full(self):
        for count_row in range(self.field_size):
            for count_column in range(self.field_size):
                if self.board[count_row][count_column] == ' ':
                    return False
        return True

    def check_winner(self, player):
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False


def quantiti_check(size, array):
    ''''
    Функция для определения значения хода с клавиатуры.
    Функция принимает заданные размеры поля и информацию о занятых ячейках,
    проверяет корректность введённых данных,
    после чего возвращает значения координат поля.
    '''
    while True:
        try:
            row = int(input('Введите номер строки: '))
            if row < 0 or row >= size:
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            if column < 0 or column >= size:
                raise FieldIndexError
            if array[row][column] != ' ':
                raise CellOcupiedError

        except FieldIndexError:
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{size}'
            )
            print('Введите значение заново')
            continue
        except ValueError:
            print('Буквы вводить нельзя, только числа')
            print(
                'Пожалуйста, введите значение для строки заново '
                'и столбца заново'
            )
            continue
        except CellOcupiedError:
            print('Попытка изменить занятую ячейку')
            continue
        except Exception as e:
            print(f'Возникла ошибка {e}')
            continue
        else:
            return row, column


def save_result(player):
    with open('results.txt', 'a', encoding='utf-8') as text:
        text.write(player + '\n')
