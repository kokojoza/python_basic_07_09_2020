from typing import List, Dict, Tuple, Union
from itertools import cycle
import random


def create_user(bot=False) -> Dict[str, Union[str, bool, List]]:
    user = {
        'name': 'R2D2' if bot else input('Ваше имя\n'),
        'symbol': 'O' if bot else 'X',
        'is_bot': bot,
        'log': [],
    }
    return user


def create_board() -> Dict[str, Union[List[List[int]], List[Tuple[int, int]]]]:
    board = {
        'board': [[0, 0, 0] for _ in range(3)],
        'variants': [(x, y) for x in range(3) for y in range(3)]
    }
    return board


def ask_step(user: Dict[str, Union[str, bool, List]], board: Dict):
    if user['is_bot']:
        step = random.choice(board['variants'])
    else:
        while True:
            user_input = input('Введите координаты через пробел целые числа от 1 до 3')

            if all([itm.isdigit() and 0 < int(itm) <= 3 for itm in user_input.split()]):
                step = tuple(int(itm) - 1 for itm in user_input.split())
                if step not in board['variants']:
                    print('LOG Ячейка занята')
                    continue
                break
            print('LOG Ошибка ввода')
    board['variants'].remove(step)
    return step


def set_step(x: int,
             y: int,
             user: Dict[str, Union[str, bool, List]],
             board: Dict) -> bool:
    if not board['board'][x][y]:
        board['board'][x][y] = user
        return True
    return False


def is_win_line(line) -> bool:
    return isinstance(line[0], Dict) and line.count(line[0]) == len(line)


def check_board(board):
    for line_column in zip(board['board'], zip(*board['board'])):
        for check in line_column:
            if is_win_line(check):
                return True, check[0]

    # проверка диагоналей
    if is_win_line([board['board'][idx][idx] for idx in range(0, 3)]):
        return True, board['board'][0][0]
    elif is_win_line([board['board'][idx][n] for idx, n in zip(range(0, 3), range(2, -1, -1))]):
        return True, board[0][-1]

    return False, None


def print_board(board):
    p_board = '#\n'.join(
        [f"{line_idx}#" + '|'.join([str(itm['symbol']) if isinstance(itm, dict) else '_' for itm in line])
         for line_idx, line in enumerate(board['board'], 1)]) + "#"
    print(f"{'##1#2#3#'}\n" + p_board + f"\n{'##1#2#3#'}\n")


def tic_tac_toe():
    user1 = create_user(False)
    user2 = create_user(True)
    board = create_board()
    for user in cycle((user1, user2)):
        print_board(board)
        print(f'{"*" * 5}-{user["name"]}-{"*" * 5}')
        x, y = ask_step(user, board)
        set_step(x, y, user, board)
        game_result = check_board(board)
        if game_result[0]:
            print(f'победил игрок {game_result[1]["name"]}')
            break


if __name__ == '__main__':
    game = tic_tac_toe()
