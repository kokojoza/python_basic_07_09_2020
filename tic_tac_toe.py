from typing import Tuple, List, Optional
import random
from itertools import cycle


class UserInterface:

    @staticmethod
    def game_mode():
        ask_str = """Ирать будете против игрок или компьютера?
            введите нужную цифру:
            1 - Против комьпьтера
            2 - Против игрока
        """
        while True:
            try:
                answer = int(input(ask_str)) - 1
                return answer
            except ValueError:
                print('Неверный ввод')
                continue

    @staticmethod
    def step(user: "User") -> Tuple[int]:
        # todo слишком много копипасты и надо разнести логику
        print(f'{"#" * 5}Ход {user}{"#" * 5}')
        while True:
            coords = input('Введте координаты через пробел\n например: 1 2\n')
            try:
                result = tuple(int(itm) - 1 for itm in coords.split() if itm.isdigit())
            except ValueError:
                print('Ошибка ввода координат введите 2 числа через пробел')
                continue

            if not result or not all(map(lambda x: x in range(3), result)) or len(result) != 2:
                print('Ошибка ввода координат введите 2 числа через пробел')
                continue

            return result

    @staticmethod
    def hello():
        help_str = """Классическая игра крестики нолики"""
        print(help_str)

    @staticmethod
    def bye():
        print('Досвидания')

    @staticmethod
    def hello_user(user: "User"):
        print(f"{user} с Символом {user.symbol} зарегистрирован в игре")

    @staticmethod
    def user_win(user: "User", game_step):
        print(f'Победитель {user} на {game_step} ходу')

    @staticmethod
    def standoff():
        print('НИЧЬЯ - Больше ходов совершить нельзя игра завершена')


class User:
    __bot_names = (
        'WALLY',
        'R2D2',
        'C3PO',
        'FEDOR'
    )
    __steps = []

    def __init__(self, name, symbol, is_bot=True):
        self.name = name
        self.is_bot = is_bot
        self.symbol = symbol
        UserInterface.hello_user(self)

    @classmethod
    def create_user(cls, symbol):
        while True:
            name = input(f'введите ваше имя игрока с символом {symbol}\n')
            if not name:
                print('необходимо ввести имя или exit для выхода')
            elif name == 'exit':
                print('До новых встреч')
                break
            else:
                return cls(name.title(), symbol, False)

    @classmethod
    def create_bot(cls, symbol):
        return cls(random.choice(cls.__bot_names), symbol, True)

    def step(self, board):
        if self.is_bot:
            coords = self.__auto_step(board)
        elif not self.is_bot:
            while True:
                coords = UserInterface.step(self)
                if not isinstance(board[coords[0]][coords[1]], User):
                    break
                print('Ячейка занята')
        else:
            assert False, 'Что-то не так это и не бот и не игрок, а кто?'

        board.set_step(self, coords)
        self.__steps.append(coords)

    @staticmethod
    def __auto_step(board: "Board"):
        return random.choice(board.free_coord)

    def __str__(self):
        return f'{"БОТ" if self.is_bot else "Игрок"} {self.name}'


class Board:
    __variants = [(n, m) for n in range(3) for m in range(3)]

    def __init__(self):
        self.__board: List[List[Optional[int, User]]] = [[0, 0, 0] for _ in range(3)]

    def __str__(self):
        # todo переделать вывод игровой доски
        result = '#\n'.join(
            [f"{line_idx}#" + '|'.join([str(itm.symbol) if isinstance(itm, User) else '_' for itm in line])
             for line_idx, line in enumerate(self.__board, 1)]) + "#"
        return f"{'##1#2#3#'}\n" + result + f"\n{'##1#2#3#'}\n"

    def set_step(self, user: User, coords: Tuple[int, int]):
        self.__board[coords[0]][coords[1]] = user
        self.__variants.remove(coords)

    @property
    def free_coord(self):
        return tuple(self.__variants)

    def __iter__(self):
        return self.__board.__iter__()

    def __getitem__(self, item):
        return self.__board[item]


class Lobby:
    __users = []
    __game_step_num = 0

    def __init__(self):
        self.board = Board()

    def start_game(self):
        UserInterface.hello()
        self.create_users()
        print(self.board)
        for user in cycle(self.__users):
            self.__game_step_num += 1
            user.step(self.board)
            step_result = self.check_board()
            print(self.board)
            if step_result[0]:
                UserInterface.user_win(step_result[1], self.__game_step_num)
                break

            if self.__game_step_num >= 9:
                UserInterface.standoff()
                break

    def create_users(self):
        game_mode = UserInterface.game_mode()
        if not game_mode:
            self.__users.extend((User.create_user("X"), User.create_bot("O")))
        elif game_mode == 1:
            self.__users.extend((User.create_user("X"), User.create_user("O")))
        else:
            assert game_mode in (0, 1), 'Неподдерживаемый режим игры'

    def check_board(self):
        # проверка линий и колонок
        for line_column in zip(self.board, zip(*self.board)):
            for check in line_column:
                if self.is_win_line(check):
                    return True, check[0]

        # проверка диагоналей
        if self.is_win_line([self.board[idx][idx] for idx in range(0, 3)]):
            return True, self.board[0][0]
        elif self.is_win_line([self.board[idx][n] for idx, n in zip(range(0, 3), range(2, -1, -1))]):
            return True, self.board[0][-1]

        return False, None

    @staticmethod
    def is_win_line(line) -> bool:
        return isinstance(line[0], User) and line.count(line[0]) == len(line)


if __name__ == '__main__':
    lobby = Lobby()
    lobby.start_game()
