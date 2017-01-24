"""Проверка: допустимое значение числа"""
def range_int(low_value, higt_value, input_text, message = "Число вне диапазона"):
    try:
        variable = int(input(input_text))
        """Проверка: допустимое значение числа"""
        if variable in range(low_value, higt_value + 1):
            return variable
        else:
            print(message)
            return range_int(low_value, higt_value, input_text, message="Число вне диапазона")
    except ValueError:
        print("Вы ввели не число!")
        return range_int(low_value, higt_value, input_text, message="Число вне диапазона")


def search_char(letter):
    for char in range(26):
        if ascii_letters[char] == letter.lower():
            return char + 1
            break
    print('Введен не верный символ, необходимо "A-Z"')


class Board(object):
    """docstring for Board"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generateBoard(self):
        board = []
        count_line = 0
        alphabet = " ".join(ascii_letters)
        board.append(["XX"] + [alphabet[:self.x * 2 - 1]])
        for line in range(self.y):
            count_line += 1
            board.append([str("{:02d}".format(count_line))] + ["O"] * self.x)
        return(board)

    def modificateBoard(self, board_1, board_2):
        modificate_board = []
        for line in range(self.y + 1):
            modificate_board.append(board_1[line] + [" "] * 15 + board_2[line])
        return(modificate_board)

    def printBoard(self, board, message="{:*^55}".format(" Твоя доска. ") + "{:*^55}".format(" Доска соперника. ")):
        print(message)
        for row in board:
            print("{:^110}".format(" ".join(row)))


class MyShips(Board):

    def set_all_ships_cords(self):
        self.all_ship_coords = []

    def choose_ship(self, player_name, board):
        self.player_name = player_name
        self.board = board
        all_ships = {1:0, 2:0, 3:1, 4:1}  # 1:4 == 1 палубный корабль 4 штук
        num_ships = 2


        def ship_range(remain):
            for ship in range(remain):
                type_ship = range_int(1, 4, "\n" + str(player_name) + ": Количество палуб коробля (1-4) ")
                if all_ships[type_ship] > 0:
                    coordinates = "1a1"
                    while not coordinates[0].isalpha() or not coordinates[0] in ascii_letters or \
                            not coordinates[1].isdigit() or coordinates[1] == "0" or \
                            not coordinates[2].isdigit() or coordinates[2] != "0":
                        coordinates = input(str(player_name) + ": Введите координаты (Например B4): ")
                        coordinates += "023"

                    ship_x = search_char(coordinates[0])
                    if len(coordinates) == 5:
                        ship_y = int(coordinates[1])
                    elif len(coordinates) == 6:
                        ship_y = int(coordinates[1] + coordinates[2])
                    else:
                        print("Ошибка с координатами")

                    if type_ship == 1:
                        coords = []
                        coords.append(ship_x)
                        coords.append(ship_y)
                        if coords in self.all_ship_coords or \
                                        [coords[0] + 1, coords[1]] in self.all_ship_coords or \
                                        [coords[0] - 1, coords[1]] in self.all_ship_coords or \
                                        [coords[0] + 1, coords[1] + 1] in self.all_ship_coords or \
                                        [coords[0] + 1, coords[1] - 1] in self.all_ship_coords or \
                                        [coords[0] - 1, coords[1] + 1] in self.all_ship_coords or \
                                        [coords[0] - 1, coords[1] - 1] in self.all_ship_coords or \
                                        [coords[0], coords[1] + 1] in self.all_ship_coords or \
                                        [coords[0], coords[1] - 1] in self.all_ship_coords:
                            print("\n" + str(player_name) + ": Слишком близко к соседнему кораблю")
                            print(all_ships)
                            if sum(all_ships.values()) != 0:
                                ship_range(remain - ship)
                        else:
                            all_ships[type_ship] -= 1
                            self.all_ship_coords.append(coords)
                            board[ship_y][ship_x] = u'\u2588'
                            os.system('cls')
                            self.printBoard(board, message="{:*^110}".format(" " + str(player_name) + "  Осталось расставить " + str(sum(all_ships.values())) + " кораблей "))
                            print(all_ships)
                            print(self.all_ship_coords)
                    else:
                        ship_position = range_int(1, 2, str(player_name) + ": Размещение корабля(1-горизонтально, 2-вертикально): ")

                        if ship_position == 1:
                            test_result = 0
                            """ Проверка всех палуб корабля """
                            for x in range(type_ship):
                                coords = []
                                coords.append(ship_x + x)
                                coords.append(ship_y)
                                if coords in self.all_ship_coords or \
                                                [ship_x + type_ship, coords[1]] in self.all_ship_coords or \
                                                [ship_x - 1, coords[1]] in self.all_ship_coords or \
                                                [coords[0] + 1, coords[1] + 1] in self.all_ship_coords or \
                                                [coords[0] + 1, coords[1] - 1] in self.all_ship_coords or \
                                                [coords[0] - 1, coords[1] + 1] in self.all_ship_coords or \
                                                [coords[0] - 1, coords[1] - 1] in self.all_ship_coords or \
                                                [coords[0], coords[1] + 1] in self.all_ship_coords or \
                                                [coords[0], coords[1] - 1] in self.all_ship_coords or ship_x + type_ship > 11:
                                    print("\n" + str(player_name) + ": Близко к соседнему кораблю либо за пределами доски")
                                    print(all_ships)
                                    if sum(all_ships.values()) != 0:
                                        ship_range(remain - ship)
                                else:
                                    test_result += 1
                            """ Если проверка пройдена - печатаем все палубы на доске """
                            if test_result == type_ship:
                                all_ships[type_ship] -= 1
                                for x in range(type_ship):
                                    coords = []
                                    coords.append(ship_x + x)
                                    coords.append(ship_y)
                                    self.all_ship_coords.append(coords)
                                    board[ship_y][ship_x + x] = u'\u2588'
                                    os.system('cls')
                                    self.printBoard(board, message="{:*^110}".format(" " + str(player_name) + " Осталось расставить " + str(sum(all_ships.values())) + " кораблей "))
                                print(all_ships)
                                print(self.all_ship_coords)

                        elif ship_position == 2:
                            test_result = 0
                            """ Проверка всех палуб корабля """
                            for y in range(type_ship):
                                coords = []
                                coords.append(ship_x)
                                coords.append(ship_y + y)
                                if coords in self.all_ship_coords or \
                                                [coords[0] + 1, coords[1]] in self.all_ship_coords or \
                                                [coords[0] - 1, coords[1]] in self.all_ship_coords or \
                                                [coords[0] + 1, coords[1] + 1] in self.all_ship_coords or \
                                                [coords[0] + 1, coords[1] - 1] in self.all_ship_coords or \
                                                [coords[0] - 1, coords[1] + 1] in self.all_ship_coords or \
                                                [coords[0] - 1, coords[1] - 1] in self.all_ship_coords or \
                                                [coords[0], ship_y + type_ship] in self.all_ship_coords or \
                                                [coords[0], ship_y - 1] in self.all_ship_coords or ship_y + type_ship > 11:
                                    print("\n" + str(player_name) + ": Близко к соседнему кораблю либо за пределами доски")
                                    print(all_ships)
                                    if sum(all_ships.values()) != 0:
                                        ship_range(remain - ship)
                                else:
                                    test_result += 1
                            """ Если проверка пройдена - печатаем все палубы на доске """
                            if test_result == type_ship:
                                all_ships[type_ship] -= 1
                                for y in range(type_ship):
                                    coords = []
                                    coords.append(ship_x)
                                    coords.append(ship_y + y)
                                    self.all_ship_coords.append(coords)
                                    board[ship_y + y][ship_x] = u'\u2588'
                                    os.system('cls')
                                    self.printBoard(board, message="{:*^110}".format(" " + str(player_name) + " Осталось расставить " + str(sum(all_ships.values())) + " кораблей "))
                                print(all_ships)
                                print(self.all_ship_coords)
                else:
                    print("\n" + str(player_name) + ": Кораблей данного типа больше нет")
                    print(all_ships)
                    if sum(all_ships.values()) != 0:
                        ship_range(remain - ship)
            return board

        board = ship_range(num_ships)
        return board

class LoseOrWin(Board):
    """Нужен модуль - from random import randint"""

    def score(self, show_my_board, show_comp_board, hide_comp_board):
        self.win = 0

        board = self.modificateBoard(show_my_board, show_comp_board)
        self.printBoard(board)

        coordinates = "1a1"
        while not coordinates[0].isalpha() or not coordinates[0] in ascii_letters or \
                not coordinates[1].isdigit() or coordinates[1] == "0" or \
                not coordinates[2].isdigit() or coordinates[2] != "0":
            coordinates = input("\n" + "Введите координаты (Например B4): ")
            coordinates += "023"

        guess_alpha = coordinates[0]
        guess_col = search_char(guess_alpha)
        if len(coordinates) == 5:
            guess_row = int(coordinates[1])
        elif len(coordinates) == 6:
            guess_row = int(coordinates[1] + coordinates[2])
        os.system('cls')


        if hide_comp_board[guess_row][guess_col] == u'\u2588': # Знак █ █ █ Unicode
            print("\n" + "{:^110}".format(" Ты попал! ") + "\n")
            if guess_row == 10 and guess_col == 10:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row - 1][guess_col - 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row - 1][guess_col - 1] = "*"

            elif guess_row == 10 and guess_col > 1:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row - 1][guess_col + 1] = "*"
                show_comp_board[guess_row - 1][guess_col - 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row - 1][guess_col + 1] = "*"
                hide_comp_board[guess_row - 1][guess_col - 1] = "*"

            elif guess_row == 10 and guess_col == 1:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row - 1][guess_col + 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row - 1][guess_col + 1] = "*"

            elif guess_row > 1 and guess_col == 10:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row - 1][guess_col - 1] = "*"
                show_comp_board[guess_row + 1][guess_col - 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row - 1][guess_col - 1] = "*"
                hide_comp_board[guess_row + 1][guess_col - 1] = "*"

            elif guess_row == 1 and guess_col == 10:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row + 1][guess_col - 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row + 1][guess_col - 1] = "*"

            elif guess_row == 1 and guess_col == 1:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row + 1][guess_col + 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row + 1][guess_col + 1] = "*"

            elif guess_row == 1 and guess_col > 1:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row + 1][guess_col + 1] = "*"
                show_comp_board[guess_row + 1][guess_col - 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row + 1][guess_col + 1] = "*"
                hide_comp_board[guess_row + 1][guess_col - 1] = "*"

            elif guess_row > 1 and guess_col == 1:
                show_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                show_comp_board[guess_row - 1][guess_col + 1] = "*"
                show_comp_board[guess_row + 1][guess_col + 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591'  # Знак ... █... Unicode
                hide_comp_board[guess_row - 1][guess_col + 1] = "*"
                hide_comp_board[guess_row + 1][guess_col + 1] = "*"

            else:
                show_comp_board[guess_row][guess_col] = u'\u2591' # Знак ... █... Unicode
                show_comp_board[guess_row + 1][guess_col + 1] = "*"
                show_comp_board[guess_row - 1][guess_col + 1] = "*"
                show_comp_board[guess_row + 1][guess_col - 1] = "*"
                show_comp_board[guess_row - 1][guess_col - 1] = "*"

                hide_comp_board[guess_row][guess_col] = u'\u2591' # Знак ... █... Unicode
                hide_comp_board[guess_row + 1][guess_col + 1] = "*"
                hide_comp_board[guess_row - 1][guess_col + 1] = "*"
                hide_comp_board[guess_row + 1][guess_col - 1] = "*"
                hide_comp_board[guess_row - 1][guess_col - 1] = "*"

            self.win += 1
        else:
            if (guess_row < 0 or guess_row > len(show_my_board)) or (guess_col < 0 or guess_col > len(show_my_board)):
                print("\n" + "{:^110}".format(" Oops, введены координаты за пределами доски. ") + "\n")
            elif show_comp_board[guess_row][guess_col] == u'\u2588' or show_comp_board[guess_row][guess_col] == "*":
                print("\n" + "{:^110}".format(" Будь внимательнее! Ты уже стрелял по этой точке. ") + "\n")
            else:
                print("\n" + "{:^110}".format(" Ты промазал! ") + "\n")
                show_comp_board[guess_row][guess_col] = "*"
                hide_comp_board[guess_row][guess_col] = "*"
        board = self.modificateBoard(show_my_board, show_comp_board)
        self.printBoard(board)

        input("\n" + "Любая кнопка чтобы продолжить: ")
        os.system('cls')

        return self.win, hide_comp_board

###################################################################################################################

if __name__ == '__main__':

    from random import randint
    from string import ascii_letters
    from datetime import datetime
    import openpyxl
    import os

    os.system('cls')
    x = 10 # range_int(5, 20, "Введите ширину доски: ", "Допустимая ширина доски 5 - 20")
    y = 10 # range_int(5, 20, "Введите высоту доски: ", "Допустимая высота доски 5 - 20")

    player_one_board = Board(x, y)
    test_board = player_one_board.generateBoard()
    print_test_board = player_one_board.printBoard(test_board, "{:*^110}".format(" Игровая доска "))
    ships_1 = MyShips(x, y)
    ships_1.set_all_ships_cords()
    board_player_one = ships_1.choose_ship("Игрок №1", test_board)

    input("\n" + "Любая кнопка чтобы продолжить: ")
    os.system('cls')

    player_two_board = Board(x, y)
    test_board = player_two_board.generateBoard()
    print_test_board = player_two_board.printBoard(test_board, "{:*^110}".format(" Игровая доска "))
    ships_2 = MyShips(x, y)
    ships_2.set_all_ships_cords()
    board_player_two = ships_2.choose_ship("Игрок №2", test_board)

    attack_board_player_1 = player_one_board.generateBoard()
    attack_board_player_2 = player_two_board.generateBoard()

    player_1 = LoseOrWin(x, y)
    player_2 = LoseOrWin(x, y)

    input("\n" + "Любая кнопка чтобы продолжить: ")
    os.system('cls')

    turn = x * y
    batch = 0
    game_score_1 = 0
    game_score_2 = 0
    for batch in range(turn):

        if batch % 2 == 0:
            print("\n" + "{:^110}".format(" Ход игрока №1 ") + "\n")
            round_score_1, board_player_two = player_1.score(board_player_one, attack_board_player_1, board_player_two)
            game_score_1 += round_score_1
            print("Игрок №1 " + str(game_score_1))
            if game_score_1 == 7:
                print("Игрок 1 победил!")
                break
        else:
            print("\n" + "{:^110}".format(" Ход игрока №2 ") + "\n")
            round_score_2, board_player_one = player_2.score(board_player_two, attack_board_player_2, board_player_one)
            game_score_2 += round_score_2
            print("Игрок №2 " + str(game_score_2))
            if game_score_2 == 7:
                print("Игрок 2 победил!")
                break