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


def corrdinates_on_board(y, x):
    if y[0] > 0 and y[0] < 11 and x[0] > 0 and x[0] < 11:
        return True
    else:
        return False


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
            board.append([str("{:02d}".format(count_line))] + [u'\u00B7'] * self.x)
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
        self.all_ship_coords = [[], [], [], [], [], [], [], [], [], []]

    def choose_ship(self, player_name, board, random_status):
        self.player_name = player_name
        self.board = board
        all_ships = {1:4, 2:3, 3:2, 4:1}  # 1:4 == 1 палубный корабль 4 штук
        num_ships = 10
        self.one_more_chance = 1

        def ship_range(remain):
            if sum(all_ships.values()) > 0:
                for ship in range(remain):
                    if random_status == 2:
                        if sum(all_ships.values()) > 0:
                            type_ship = randint(1, 4)
                            while all_ships[type_ship] == 0:
                                type_ship = randint(1, 4)
                        else:
                            break
                        if all_ships[type_ship] > 0:
                            ship_x = randint(1, 10)
                            ship_y = randint(1, 10)
                        else:
                            break

                    elif random_status == 1:
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

                        else:
                            print("\n" + str(player_name) + ": Кораблей данного типа больше нет")
                            print(all_ships)
                            if sum(all_ships.values()) != 0:
                                ship_range(remain - ship)
                                break

                    if type_ship == 1:
                        coords = []
                        coords.append(ship_x)
                        coords.append(ship_y)
                        for counter in range(len(self.all_ship_coords)):
                            if coords in self.all_ship_coords[counter] or \
                                            [coords[0] + 1, coords[1]] in self.all_ship_coords[counter] or \
                                            [coords[0] - 1, coords[1]] in self.all_ship_coords[counter] or \
                                            [coords[0] + 1, coords[1] + 1] in self.all_ship_coords[counter] or \
                                            [coords[0] + 1, coords[1] - 1] in self.all_ship_coords[counter] or \
                                            [coords[0] - 1, coords[1] + 1] in self.all_ship_coords[counter] or \
                                            [coords[0] - 1, coords[1] - 1] in self.all_ship_coords[counter] or \
                                            [coords[0], coords[1] + 1] in self.all_ship_coords[counter] or \
                                            [coords[0], coords[1] - 1] in self.all_ship_coords[counter]:
                                if random_status == 1:
                                    print("\n" + str(player_name) + ": Слишком близко к соседнему кораблю")
                                    print(all_ships)
                                ship_range(remain - ship)
                                break
                        else:
                            all_ships[type_ship] -= 1
                            self.all_ship_coords[sum(all_ships.values())].append(coords)
                            board[ship_y][ship_x] = u'\u2588'
                            self.printBoard(board, message="{:*^110}".format(" " + str(player_name) + "  Осталось расставить " + str(sum(all_ships.values())) + " кораблей "))
                            print(all_ships)
                            print(self.all_ship_coords)
                    else:
                        if random_status == 2:
                            ship_position = randint(1, 2)
                        else:
                            ship_position = range_int(1, 2, str(player_name) + ": Размещение корабля(1-горизонтально, 2-вертикально): ")

                        if ship_position == 1:
                            test_result = 0
                            """ Проверка всех палуб корабля """
                            for x in range(type_ship):
                                coords = []
                                coords.append(ship_x + x)
                                coords.append(ship_y)
                                for counter in range(len(self.all_ship_coords)):
                                    if coords in self.all_ship_coords[counter] or \
                                                    [coords[0] + 1, coords[1]] in self.all_ship_coords[counter] or \
                                                    [coords[0] - 1, coords[1]] in self.all_ship_coords[counter] or \
                                                    [coords[0] + 1, coords[1] + 1] in self.all_ship_coords[counter] or \
                                                    [coords[0] + 1, coords[1] - 1] in self.all_ship_coords[counter] or \
                                                    [coords[0] - 1, coords[1] + 1] in self.all_ship_coords[counter] or \
                                                    [coords[0] - 1, coords[1] - 1] in self.all_ship_coords[counter] or \
                                                    [coords[0], coords[1] + 1] in self.all_ship_coords[counter] or \
                                                    [coords[0], coords[1] - 1] in self.all_ship_coords[counter] or ship_x + type_ship > 11:
                                        if random_status == 1:
                                            print("\n" + str(player_name) + ": Близко к соседнему кораблю либо за пределами доски")
                                            print(all_ships)
                                        ship_range(remain - ship)
                                        break
                                else:
                                    test_result += 1
                            """ Если проверка пройдена - печатаем все палубы на доске """
                            if test_result == type_ship:
                                all_ships[type_ship] -= 1
                                for x in range(type_ship):
                                    coords = []
                                    coords.append(ship_x + x)
                                    coords.append(ship_y)
                                    self.all_ship_coords[sum(all_ships.values())].append(coords)
                                    board[ship_y][ship_x + x] = u'\u2588'
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
                                for counter in range(len(self.all_ship_coords)):
                                    if coords in self.all_ship_coords[counter] or \
                                                    [coords[0] + 1, coords[1]] in self.all_ship_coords[counter] or \
                                                    [coords[0] - 1, coords[1]] in self.all_ship_coords[counter] or \
                                                    [coords[0] + 1, coords[1] + 1] in self.all_ship_coords[counter] or \
                                                    [coords[0] + 1, coords[1] - 1] in self.all_ship_coords[counter] or \
                                                    [coords[0] - 1, coords[1] + 1] in self.all_ship_coords[counter] or \
                                                    [coords[0] - 1, coords[1] - 1] in self.all_ship_coords[counter] or \
                                                    [coords[0], coords[1] + 1] in self.all_ship_coords[counter] or \
                                                    [coords[0], coords[1] - 1] in self.all_ship_coords[counter] or ship_y + type_ship > 11:
                                        if random_status == 1:
                                            print("\n" + str(player_name) + ": Близко к соседнему кораблю либо за пределами доски")
                                            print(all_ships)
                                        ship_range(remain - ship)
                                        break
                                else:
                                    test_result += 1
                            """ Если проверка пройдена - печатаем все палубы на доске """
                            if test_result == type_ship:
                                all_ships[type_ship] -= 1
                                for y in range(type_ship):
                                    coords = []
                                    coords.append(ship_x)
                                    coords.append(ship_y + y)
                                    self.all_ship_coords[sum(all_ships.values())].append(coords)
                                    board[ship_y + y][ship_x] = u'\u2588'
                                    self.printBoard(board, message="{:*^110}".format(" " + str(player_name) + " Осталось расставить " + str(sum(all_ships.values())) + " кораблей "))
                                print(all_ships)
                                print(self.all_ship_coords)
            return board

        board = ship_range(num_ships)
        return board , self.all_ship_coords


class LoseOrWin(Board):
    """Нужен модуль - from random import randint"""
    def win_score(self):
        self.win = 0
        self.strike_ship = [[], [], [], [], [], [], [], [], [], []]
        self.my_strikes = []
        self.one_more_chance = 0
        self.kill_allship = True

    def score(self, show_my_board, show_comp_board, hide_comp_board, ship_coords, random_status, gui_status=0):

        board = self.modificateBoard(show_my_board, show_comp_board)
        self.printBoard(board)


        try:
            if show_comp_board[self.shoot_row][self.shoot_col] == "X":  # Возврат доски в нормальное состояние (обнуление предыдущего попадания)
                show_comp_board[self.shoot_row][self.shoot_col] = "*"
            elif show_comp_board[self.shoot_row][self.shoot_col] == u'\u2593':
                show_comp_board[self.shoot_row][self.shoot_col] = u'\u2591'
        except AttributeError:
            pass



        if random_status == 2:  # Рандомно стреляем по кораблям
            if self.one_more_chance == 2 and not self.kill_allship:  # Если попал по кораблю но ещё не потопил

                if self.ship_point_counter == 1:  # Количество подбитых палуб только 1 штука!

                    guess_col = self.shoot_col
                    guess_row = self.shoot_row
                    while guess_col < 1 or guess_col > 10 or guess_row < 1 or guess_row > 10 or \
                                    show_comp_board[guess_row][guess_col] != u'\u00B7' or show_comp_board[guess_row][guess_col] == u'\u2591': # Знак ... █... Unicode
                        guess_col = randint(self.my_strikes[-1][0] - 1, self.my_strikes[-1][0] + 1)
                        guess_row = randint(self.my_strikes[-1][1] - 1, self.my_strikes[-1][1] + 1)

                elif self.ship_point_counter > 1: # Количество подбитых палуб больше 1 шт подряд!

                    if self.my_strikes[-1][0] - self.my_strikes[-2][0] == 0:  # Значит координаты не меняются по иксу (колонна)
                        if self.my_strikes[-1][1] + 1 < 11 and \
                                        show_comp_board[self.shoot_row + 1][self.shoot_col] == u'\u00B7' :
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[-1][1] + 1
                        elif self.my_strikes[-1][1] - 1 > 0 and \
                                        show_comp_board[self.shoot_row - 1][self.shoot_col] == u'\u00B7' :
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[-1][1] - 1
                        elif self.my_strikes[-self.ship_point_counter][1] + 1 < 11 and \
                                        show_comp_board[self.my_strikes[-self.ship_point_counter][1] + 1][self.shoot_col] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[- self.ship_point_counter][1] + 1
                        elif self.my_strikes[-self.ship_point_counter][1] - 1 > 0 and \
                                        show_comp_board[self.my_strikes[-self.ship_point_counter][1] - 1][self.shoot_col] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[- self.ship_point_counter][1] - 1
                        else:
                            print("=================== ВОЗМОЖНО Ошибка координат 2.1")
                            guess_col = self.shoot_col
                            if self.my_strikes[-1][1] - self.my_strikes[-2][1] == 1:
                                guess_row = self.my_strikes[-1][1] - self.ship_point_counter
                            elif self.my_strikes[-1][1] - self.my_strikes[-2][1] == -1:
                                guess_row = self.my_strikes[-1][1] + self.ship_point_counter

                    elif self.my_strikes[-1][1] - self.my_strikes[-2][1] == 0: # Значит координаты не меняются по игрику (ряд)
                        if self.my_strikes[-1][0] + 1 < 11 and \
                                        show_comp_board[self.shoot_row][self.shoot_col + 1] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0] + 1
                            guess_row = self.my_strikes[-1][1]
                        elif self.my_strikes[-1][0] - 1 > 0 and \
                                        show_comp_board[self.shoot_row][self.shoot_col - 1] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0] - 1
                            guess_row = self.my_strikes[-1][1]

                        elif self.my_strikes[-self.ship_point_counter][1] + 1 < 11 and \
                                        show_comp_board[self.shoot_row][self.my_strikes[-self.ship_point_counter][0] + 1] == u'\u00B7':
                            guess_col = self.my_strikes[- self.ship_point_counter][0] + 1
                            guess_row = self.my_strikes[-1][1]
                        elif self.my_strikes[-self.ship_point_counter][1] - 1 > 0 and \
                                        show_comp_board[self.shoot_row][self.my_strikes[-self.ship_point_counter][0] - 1] == u'\u00B7':
                            guess_col = self.my_strikes[- self.ship_point_counter][0] - 1
                            guess_row = self.my_strikes[-1][1]
                        else:
                            print("=================== ВОЗМОЖНО Ошибка координат 2.2")
                            guess_row = self.shoot_row
                            if self.my_strikes[-1][0] - self.my_strikes[-2][0] == 1:
                                guess_col = self.my_strikes[-1][0] - self.ship_point_counter
                            elif self.my_strikes[-1][0] - self.my_strikes[-2][0] == -1:
                                guess_col = self.my_strikes[-1][0] + self.ship_point_counter

                    elif self.my_strikes[-1][0] - self.my_strikes[-3][0] == 0:  # Значит координаты не меняются по иксу (колонна)
                        if self.my_strikes[-1][1] + 1 < 11 and \
                                        show_comp_board[self.shoot_row + 1][self.shoot_col] == u'\u00B7' :
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[-1][1] + 1
                        elif self.my_strikes[-1][1] - 1 > 0 and \
                                        show_comp_board[self.shoot_row - 1][self.shoot_col] == u'\u00B7' :
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[-1][1] - 1
                        elif self.my_strikes[-self.ship_point_counter][1] + 1 < 11 and \
                                        show_comp_board[self.my_strikes[-self.ship_point_counter][1] + 1][self.shoot_col] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[- self.ship_point_counter][1] + 1
                        elif self.my_strikes[-self.ship_point_counter][1] - 1 > 0 and \
                                        show_comp_board[self.my_strikes[-self.ship_point_counter][1] - 1][self.shoot_col] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[- self.ship_point_counter][1] - 1
                        else:
                            print("=================== ВОЗМОЖНО Ошибка координат 2.3")
                            guess_col = self.shoot_col
                            if self.my_strikes[-1][1] - self.my_strikes[-2][1] == 1:
                                guess_row = self.my_strikes[-1][1] - self.ship_point_counter
                            elif self.my_strikes[-1][1] - self.my_strikes[-2][1] == -1:
                                guess_row = self.my_strikes[-1][1] + self.ship_point_counter

                    elif self.my_strikes[-1][1] - self.my_strikes[-3][1] == 0: # Значит координаты не меняются по игрику (ряд)
                        if self.my_strikes[-1][0] + 1 < 11 and \
                                        show_comp_board[self.shoot_row][self.shoot_col + 1] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0] + 1
                            guess_row = self.my_strikes[-1][1]
                        elif self.my_strikes[-1][0] - 1 > 0 and \
                                        show_comp_board[self.shoot_row][self.shoot_col - 1] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0] - 1
                            guess_row = self.my_strikes[-1][1]

                        elif self.my_strikes[-self.ship_point_counter][1] + 1 < 11 and \
                                        show_comp_board[self.shoot_row][self.my_strikes[-self.ship_point_counter][0] + 1] == u'\u00B7':
                            guess_col = self.my_strikes[- self.ship_point_counter][0] + 1
                            guess_row = self.my_strikes[-1][1]
                        elif self.my_strikes[-self.ship_point_counter][1] - 1 > 0 and \
                                        show_comp_board[self.shoot_row][self.my_strikes[-self.ship_point_counter][0] - 1] == u'\u00B7':
                            guess_col = self.my_strikes[- self.ship_point_counter][0] - 1
                            guess_row = self.my_strikes[-1][1]
                        else:
                            print("=================== ВОЗМОЖНО Ошибка координат 2.4")
                            guess_row = self.shoot_row
                            if self.my_strikes[-1][0] - self.my_strikes[-2][0] == 1:
                                guess_col = self.my_strikes[-1][0] - self.ship_point_counter
                            elif self.my_strikes[-1][0] - self.my_strikes[-2][0] == -1:
                                guess_col = self.my_strikes[-1][0] + self.ship_point_counter

                    elif self.my_strikes[-1][0] - self.my_strikes[-4][0] == 0:  # Значит координаты не меняются по иксу (колонна)
                        if self.my_strikes[-1][1] + 1 < 11 and \
                                        show_comp_board[self.shoot_row + 1][self.shoot_col] == u'\u00B7' :
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[-1][1] + 1
                        elif self.my_strikes[-1][1] - 1 > 0 and \
                                        show_comp_board[self.shoot_row - 1][self.shoot_col] == u'\u00B7' :
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[-1][1] - 1
                        elif self.my_strikes[-self.ship_point_counter][1] + 1 < 11 and \
                                        show_comp_board[self.my_strikes[-self.ship_point_counter][1] + 1][self.shoot_col] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[- self.ship_point_counter][1] + 1
                        elif self.my_strikes[-self.ship_point_counter][1] - 1 > 0 and \
                                        show_comp_board[self.my_strikes[-self.ship_point_counter][1] - 1][self.shoot_col] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0]
                            guess_row = self.my_strikes[- self.ship_point_counter][1] - 1
                        else:
                            print("=================== ВОЗМОЖНО Ошибка координат 2.5")
                            guess_col = self.shoot_col
                            if self.my_strikes[-1][1] - self.my_strikes[-2][1] == 1:
                                guess_row = self.my_strikes[-1][1] - self.ship_point_counter
                            elif self.my_strikes[-1][1] - self.my_strikes[-2][1] == -1:
                                guess_row = self.my_strikes[-1][1] + self.ship_point_counter

                    elif self.my_strikes[-1][1] - self.my_strikes[-4][1] == 0: # Значит координаты не меняются по игрику (ряд)
                        if self.my_strikes[-1][0] + 1 < 11 and \
                                        show_comp_board[self.shoot_row][self.shoot_col + 1] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0] + 1
                            guess_row = self.my_strikes[-1][1]
                        elif self.my_strikes[-1][0] - 1 > 0 and \
                                        show_comp_board[self.shoot_row][self.shoot_col - 1] == u'\u00B7':
                            guess_col = self.my_strikes[-1][0] - 1
                            guess_row = self.my_strikes[-1][1]

                        elif self.my_strikes[-self.ship_point_counter][1] + 1 < 11 and \
                                        show_comp_board[self.shoot_row][self.my_strikes[-self.ship_point_counter][0] + 1] == u'\u00B7':
                            guess_col = self.my_strikes[- self.ship_point_counter][0] + 1
                            guess_row = self.my_strikes[-1][1]
                        elif self.my_strikes[-self.ship_point_counter][1] - 1 > 0 and \
                                        show_comp_board[self.shoot_row][self.my_strikes[-self.ship_point_counter][0] - 1] == u'\u00B7':
                            guess_col = self.my_strikes[- self.ship_point_counter][0] - 1
                            guess_row = self.my_strikes[-1][1]
                        else:
                            print("=================== ВОЗМОЖНО Ошибка координат 2.6")
                            guess_row = self.shoot_row
                            if self.my_strikes[-1][0] - self.my_strikes[-2][0] == 1:
                                guess_col = self.my_strikes[-1][0] - self.ship_point_counter
                            elif self.my_strikes[-1][0] - self.my_strikes[-2][0] == -1:
                                guess_col = self.my_strikes[-1][0] + self.ship_point_counter

            elif self.one_more_chance == 3 and not self.kill_allship: # Если уже попадал по кораблю не потопил, но потом промазал

                if self.ship_point_counter == 1:  # Количество подбитых палуб только 1 штука!

                    if show_comp_board[self.my_strikes[-1][1]][self.my_strikes[-1][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-2][1]][self.my_strikes[-2][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-3][1]][self.my_strikes[-3][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-4][1]][self.my_strikes[-4][0]] == u'\u2591': # Знак ... █... Unicode
                        guess_col = self.shoot_col
                        guess_row = self.shoot_row
                        while guess_col < 1 or guess_col > 10 or guess_row < 1 or guess_row > 10 or \
                                        show_comp_board[guess_row][guess_col] != u'\u00B7' or \
                                        show_comp_board[guess_row][guess_col] == u'\u2591':  # Знак ... █... Unicode
                            guess_col = randint(self.my_strikes[-4][0] - 1, self.my_strikes[-4][0] + 1)
                            guess_row = randint(self.my_strikes[-4][1] - 1, self.my_strikes[-4][1] + 1)

                    elif show_comp_board[self.my_strikes[-1][1]][self.my_strikes[-1][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-2][1]][self.my_strikes[-2][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-3][1]][self.my_strikes[-3][0]] == u'\u2591': # Знак ... █... Unicode
                        guess_col = self.shoot_col
                        guess_row = self.shoot_row
                        while guess_col < 1 or guess_col > 10 or guess_row < 1 or guess_row > 10 or \
                                        show_comp_board[guess_row][guess_col] != u'\u00B7' or \
                                        show_comp_board[guess_row][guess_col] == u'\u2591':  # Знак ... █... Unicode
                            guess_col = randint(self.my_strikes[-3][0] - 1, self.my_strikes[-3][0] + 1)
                            guess_row = randint(self.my_strikes[-3][1] - 1, self.my_strikes[-3][1] + 1)

                    elif show_comp_board[self.my_strikes[-1][1]][self.my_strikes[-1][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-2][1]][self.my_strikes[-2][0]] == u'\u2591': # Знак ... █... Unicode
                        guess_col = self.shoot_col
                        guess_row = self.shoot_row
                        while guess_col < 1 or guess_col > 10 or guess_row < 1 or guess_row > 10 or \
                                        show_comp_board[guess_row][guess_col] != u'\u00B7' or \
                                        show_comp_board[guess_row][guess_col] == u'\u2591':  # Знак ... █... Unicode
                            guess_col = randint(self.my_strikes[-2][0] - 1, self.my_strikes[-2][0] + 1)
                            guess_row = randint(self.my_strikes[-2][1] - 1, self.my_strikes[-2][1] + 1)
                    else:
                        print("===================Ошибка координат 3.1")

                if self.ship_point_counter > 1:  # Количество подбитых палуб больше 1 штуки!

                    if show_comp_board[self.my_strikes[-1][1]][self.my_strikes[-1][0]] == "*" and \
                                    show_comp_board[self.my_strikes[-2][1]][self.my_strikes[-2][0]] == u'\u2591': # Знак ... █... Unicode

                        if self.my_strikes[-1][0] - self.my_strikes[-2][0] == 0:  # Значит координаты не меняются по иксу (колонна)
                            guess_col = self.shoot_col
                            if self.my_strikes[-1][1] - self.my_strikes[-2][1] == 1:
                                guess_row = self.my_strikes[-1][1] - (self.ship_point_counter + 1)
                            elif self.my_strikes[-1][1] - self.my_strikes[-2][1] == -1:
                                guess_row = self.my_strikes[-1][1] + self.ship_point_counter + 1

                        elif self.my_strikes[-1][1] - self.my_strikes[-2][1] == 0:  # Значит координаты не меняются по игрику (ряд)
                            guess_row = self.shoot_row
                            if self.my_strikes[-1][0] - self.my_strikes[-2][0] == 1:
                                guess_col = self.my_strikes[-1][0] - (self.ship_point_counter + 1)
                            elif self.my_strikes[-1][0] - self.my_strikes[-2][0] == -1:
                                guess_col = self.my_strikes[-1][0] + self.ship_point_counter + 1
                    else:
                        print("===================Ошибка координат 3.2")

            else:
                guess_col = randint(1, 10)
                guess_row = randint(1, 10)
                while show_comp_board[guess_row][guess_col] == "*" or show_comp_board[guess_row][guess_col] == u'\u2591':
                    guess_col = randint(1, 10)
                    guess_row = randint(1, 10)

        else:  # Вводим координаты вручную
            if gui_status == 0:
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
            elif gui_status == 1:
                guess_col = mouse_x
                guess_row = mouse_y

        """Сохраняем данные предыдущего выстрела"""
        self.shoot_col = guess_col
        self.shoot_row = guess_row
        self.my_strikes.append([guess_col, guess_row])

        if hide_comp_board[guess_row][guess_col] == u'\u2588': # Знак █ █ █ Unicode
            print("\n" + "{:^110}".format(" Ты попал! ") + "\n")
            self.one_more_chance = 2

            """ Если попал - диагональ **** """
            show_comp_board[guess_row][guess_col] = u'\u2591' # Знак ... █... Unicode
            if corrdinates_on_board([guess_row + 1], [guess_col + 1]): show_comp_board[guess_row + 1][guess_col + 1] = "*"
            if corrdinates_on_board([guess_row - 1], [guess_col + 1]): show_comp_board[guess_row - 1][guess_col + 1] = "*"
            if corrdinates_on_board([guess_row + 1], [guess_col - 1]): show_comp_board[guess_row + 1][guess_col - 1] = "*"
            if corrdinates_on_board([guess_row - 1], [guess_col - 1]): show_comp_board[guess_row - 1][guess_col - 1] = "*"

            hide_comp_board[guess_row][guess_col] = u'\u2591' # Знак ... █... Unicode
            if corrdinates_on_board([guess_row + 1], [guess_col + 1]): hide_comp_board[guess_row + 1][guess_col + 1] = "*"
            if corrdinates_on_board([guess_row - 1], [guess_col + 1]): hide_comp_board[guess_row - 1][guess_col + 1] = "*"
            if corrdinates_on_board([guess_row + 1], [guess_col - 1]): hide_comp_board[guess_row + 1][guess_col - 1] = "*"
            if corrdinates_on_board([guess_row - 1], [guess_col - 1]): hide_comp_board[guess_row - 1][guess_col - 1] = "*"

            """ Проверка уничтожен ли корабль - спереди/сзади **** """
            self.kill_allship = False
            for ship in ship_coords:
                counter = 0
                if [guess_col, guess_row] in ship:
                    ship_type = len(ship)
                    self.strike_ship[counter].append([guess_col, guess_row])

                    if ship_type == 1:
                        self.kill_allship = True
                        if corrdinates_on_board([guess_row - 1], [guess_col]): show_comp_board[guess_row - 1][guess_col] = "*"
                        if corrdinates_on_board([guess_row + 1], [guess_col]): show_comp_board[guess_row + 1][guess_col] = "*"
                        if corrdinates_on_board([guess_row], [guess_col - 1]): show_comp_board[guess_row][guess_col - 1] = "*"
                        if corrdinates_on_board([guess_row], [guess_col + 1]): show_comp_board[guess_row][guess_col + 1] = "*"
                        if corrdinates_on_board([guess_row - 1], [guess_col]): hide_comp_board[guess_row - 1][guess_col] = "*"
                        if corrdinates_on_board([guess_row + 1], [guess_col]): hide_comp_board[guess_row + 1][guess_col] = "*"
                        if corrdinates_on_board([guess_row], [guess_col - 1]): hide_comp_board[guess_row][guess_col - 1] = "*"
                        if corrdinates_on_board([guess_row], [guess_col + 1]): hide_comp_board[guess_row][guess_col + 1] = "*"
                    else:
                        self.ship_point_counter = 0
                        for point in range(ship_type):
                            if ship[point] in self.strike_ship[counter]:
                                self.ship_point_counter +=1

                        if self.ship_point_counter == ship_type:
                            self.kill_allship = True
                            if ship[ship_type-1][0] - ship[0][0] == 0:  # Значит координаты не меняются по иксу
                                if corrdinates_on_board([ship[ship_type-1][1] + 1], [ship[0][0]]): show_comp_board[ship[ship_type-1][1] + 1][ship[0][0]] = "*"
                                if corrdinates_on_board([ship[0][1] - 1], [ship[0][0]]): show_comp_board[ship[0][1] - 1][ship[0][0]] = "*"
                                if corrdinates_on_board([ship[ship_type-1][1] + 1], [ship[0][0]]): hide_comp_board[ship[ship_type-1][1] + 1][ship[0][0]] = "*"
                                if corrdinates_on_board([ship[0][1] - 1], [ship[0][0]]): hide_comp_board[ship[0][1] - 1][ship[0][0]] = "*"
                            else:
                                if corrdinates_on_board([ship[0][1]], [ship[ship_type-1][0] + 1]): show_comp_board[ship[0][1]][ship[ship_type-1][0] + 1] = "*"
                                if corrdinates_on_board([ship[0][1]], [ship[0][0] - 1]): show_comp_board[ship[0][1]][ship[0][0] - 1] = "*"
                                if corrdinates_on_board([ship[0][1]], [ship[ship_type-1][0] + 1]): hide_comp_board[ship[0][1]][ship[ship_type-1][0] + 1] = "*"
                                if corrdinates_on_board([ship[0][1]], [ship[0][0] - 1]): hide_comp_board[ship[0][1]][ship[0][0] - 1] = "*"
                counter += 1
            self.win += 1
        else:
            if (guess_row < 0 or guess_row > len(show_my_board)) or (guess_col < 0 or guess_col > len(show_my_board)):
                print("\n" + "{:^110}".format(" Oops, введены координаты за пределами доски. ") + "\n")
                self.one_more_chance = 1
            elif show_comp_board[guess_row][guess_col] == u'\u2591' or show_comp_board[guess_row][guess_col] == "*":
                print("\n" + "{:^110}".format(" Будь внимательнее! Ты уже стрелял по этой точке. ") + "\n")
                self.one_more_chance = 1
            else:
                print("\n" + "{:^110}".format(" Ты промазал! ") + "\n")
                show_comp_board[guess_row][guess_col] = "*"
                hide_comp_board[guess_row][guess_col] = "*"
                if not self.kill_allship:
                    self.one_more_chance = 3  # Подбил корабль но не убил его до конца
                else:
                    self.one_more_chance = 0  # Просто промазал

        if show_comp_board[self.shoot_row][self.shoot_col] == "*":
            show_comp_board[self.shoot_row][self.shoot_col] = "X"
            board = self.modificateBoard(show_my_board, show_comp_board)
            self.printBoard(board)
        elif show_comp_board[self.shoot_row][self.shoot_col] == u'\u2591':
            show_comp_board[self.shoot_row][self.shoot_col] = u'\u2593'
            board = self.modificateBoard(show_my_board, show_comp_board)
            self.printBoard(board)
        else:
            board = self.modificateBoard(show_my_board, show_comp_board)
            self.printBoard(board)

        return self.win, hide_comp_board, self.one_more_chance, show_comp_board



from random import randint
from string import ascii_letters
import os
from tkinter import *
from tkinter.messagebox import *


def mouse_input(event):
    x = event.x  # canv2.canvasx(event.x)  # получаем x координату точки, в которой кликнули
    y = event.y  # canv2.canvasy(event.y)  # получаем y координату точки, в которой кликнули

    global mouse_x
    global mouse_y

    if x == 20:
        mouse_x = 1
    else:
        mouse_x = (x - 20) // 30 + 1
    if y == 20:
        mouse_y = 1
    else:
        mouse_y = (y - 20) // 30 + 1

    if  mouse_x > 0 and mouse_y > 0 and mouse_x < 11 and mouse_y < 11:
        game_gui()


def game_gui():

    gui_status = 1

    def player_one_strike():
        print("\n" + "{:^110}".format(" Ход игрока №1 ") + "\n")
        game_score_1, ships_2.board, one_more_chance_1, show_comp_board1 = player_1.score(ships_1.board,attack_board_player_1,
                                                                                          ships_2.board,ships_2.all_ship_coords,
                                                                                          random_status_game_1,gui_status)
        print_desk_gui(show_comp_board1, canv2)
        if random_status_game_2 == 1:
            print_desk_gui(ships_2.board, canv1_win2)
        print("Игрок №1 " + str(game_score_1))
        if game_score_1 == 20:
            print("Игрок 1 победил!")
            showinfo("Победа", "Игрок 1 победил!")
            after_win = askokcancel("Реванш?", "Хотите сыграть ещё одну партию?")
            if after_win == 1 and random_status_game_2 == 2:
                game_for_one()
            elif after_win == 1 and random_status_game_2 == 1:
                win2.destroy()
                game_for_two()
            elif after_win == 0:
                exit_app()

    def player_two_strike():
        print("\n" + "{:^110}".format(" Ход игрока №2 ") + "\n")
        if random_status_game_2 == 2:
            canv1.after(500)
        game_score_2, ships_1.board, one_more_chance_2, show_comp_board2 = player_2.score(ships_2.board,attack_board_player_2,
                                                                                          ships_1.board,ships_1.all_ship_coords,
                                                                                          random_status_game_2,gui_status)
        print_desk_gui(show_comp_board2, canv1)
        if random_status_game_2 == 1:
            print_desk_gui(attack_board_player_2, canv2_win2)
        print("Игрок №2 " + str(game_score_2))
        if game_score_2 == 20:
            print("Игрок 2 победил!")
            showinfo("Победа", "Игрок 2 победил!")
            after_win = askokcancel("Реванш?", "Хотите сыграть ещё одну партию?")
            if after_win == 1 and random_status_game_2 == 2:
                game_for_one()
            elif after_win == 1 and random_status_game_2 == 1:
                win2.destroy()
                game_for_two()
            elif after_win == 0:
                exit_app()

    if random_status_game_2 == 1:
        global strike_counter
        if player_1.one_more_chance == 1 or player_1.one_more_chance == 2:
            player_one_strike()
            if player_1.one_more_chance == 0 or player_1.one_more_chance == 3:
                canv2.unbind("<Button-1>")
                canv2.config(bg='#223', cursor="watch")
                canv2_win2.bind("<Button-1>", mouse_input)
                canv2_win2.config(bg='#001', cursor="target")
        elif player_2.one_more_chance == 1 or player_2.one_more_chance == 2:
            player_two_strike()
            if player_2.one_more_chance == 0 or player_2.one_more_chance == 3:
                canv2_win2.unbind("<Button-1>")
                canv2_win2.config(bg='#223', cursor="watch")
                canv2.bind("<Button-1>", mouse_input)
                canv2.config(bg='#001', cursor="target")
        elif (player_1.one_more_chance == 0 or player_1.one_more_chance == 3) and  strike_counter == 0:
            player_one_strike()
            strike_counter += 1
            if player_1.one_more_chance == 0 or player_1.one_more_chance == 3:
                canv2.unbind("<Button-1>")
                canv2.config(bg='#223', cursor="watch")
                canv2_win2.bind("<Button-1>", mouse_input)
                canv2_win2.config(bg='#001', cursor="target")
        elif(player_2.one_more_chance == 0 or player_2.one_more_chance == 3) and strike_counter == 1:
            player_two_strike()
            strike_counter -= 1
            if player_2.one_more_chance == 0 or player_2.one_more_chance == 3:
                canv2_win2.unbind("<Button-1>")
                canv2_win2.config(bg='#223', cursor = "watch")
                canv2.bind("<Button-1>", mouse_input)
                canv2.config(bg='#001', cursor = "target")

    elif random_status_game_2 == 2:
        if player_1.one_more_chance == 1 or player_1.one_more_chance == 2:
            player_one_strike()
            canv2.unbind("<Button-1>")
            canv2.config(cursor="watch")
            if player_1.one_more_chance == 0 or player_1.one_more_chance == 3: #Если я промазал то сразу же ход второго игрока
                player_two_strike()
                while player_2.one_more_chance == 1 or player_2.one_more_chance == 2:
                    player_two_strike()
            canv2.bind("<Button-1>", mouse_input)
            canv2.config(cursor="target")
        # elif player_2.one_more_chance == 1 or player_2.one_more_chance == 2: # если игрок 2 не мажет то продолжает ходить
        #     player_two_strike()
        #     while player_2.one_more_chance == 1 or player_2.one_more_chance == 2:
        #         player_two_strike()
        elif player_1.one_more_chance == 0 or player_1.one_more_chance == 3:
            player_one_strike()
            canv2.unbind("<Button-1>")
            canv2.config(cursor="watch")
            if player_1.one_more_chance == 0 or player_1.one_more_chance == 3:
                player_two_strike()
                while player_2.one_more_chance == 1 or player_2.one_more_chance == 2:
                    player_two_strike()
            canv2.bind("<Button-1>", mouse_input)
            canv2.config(cursor="target")


def game_for_one():
    canvas_clear(canv1)
    canvas_clear(canv2)

    x = 10
    y = 10

    global player_1
    global player_2
    global ships_1
    global ships_2
    global attack_board_player_1
    global attack_board_player_2
    global random_status_game_1
    global random_status_game_2

    random_status_game_1 = 1  # range_int(1, 2, "Игрок №1: Как стрелять (1 - руками, 2 - рандомно): ")
    random_status_game_2 = 2  # range_int(1, 2, "Игрок №2: Как стрелять (1 - руками, 2 - рандомно): ")

    ships_1 = MyShips(x, y)
    test_board = ships_1.generateBoard()
    ships_1.set_all_ships_cords()
    random_status_1 = 2  # range_int(1, 2, "Игрок №1: Как разместить корабли (1 - руками, 2 - рандомно): ")
    board_player_one, coords_1 = ships_1.choose_ship("Игрок №1", test_board, random_status_1)

    print_desk_gui(board_player_one, canv1)

    ships_2 = MyShips(x, y)
    test_board = ships_2.generateBoard()
    ships_2.set_all_ships_cords()
    random_status_2 = 2  # range_int(1, 2, "Игрок №2: Как разместить корабли (1 - руками, 2 - рандомно): ")
    board_player_two, coords_2 = ships_2.choose_ship("Игрок №2", test_board, random_status_2)

    player_1 = LoseOrWin(x, y)
    player_1.win_score()
    player_2 = LoseOrWin(x, y)
    player_2.win_score()

    clean_board1 = Board(x, y)
    clean_board2 = Board(x, y)
    attack_board_player_1 = clean_board1.generateBoard()
    attack_board_player_2 = clean_board2.generateBoard()


def game_for_two():
    canvas_clear(canv1)
    canvas_clear(canv2)

    global win2
    win2 = Toplevel(root)
    win2.title("Battleship 3.0 - 2 Игрок")
    win2.resizable(False,False)

    label1 = Label(win2, text="Игрок 2: Твоя доска")
    label1.grid(row=0, column=0)
    label2 = Label(win2, text="Доска соперника")
    label2.grid(row=0, column=3)

    global canv1_win2
    canv1_win2 = Canvas(win2, width=340, height=340, bg='#001', cursor="boat")
    canvas_line(canv1_win2)
    canvas_coords_name(canv1_win2)
    canv1_win2.grid(row=1, column=0)
    global canv2_win2
    canv2_win2 = Canvas(win2, width=340, height=340, bg='#223', cursor="watch")
    canvas_line(canv2_win2)
    canvas_coords_name(canv2_win2)
    canv2_win2.grid(row=1, column=3)

    canv_separator_win2 = Canvas(win2, width=50, height=10)
    canv_separator_win2.grid(row=3, column=2)

    x = 10
    y = 10

    global player_1
    global player_2
    global ships_1
    global ships_2
    global attack_board_player_1
    global attack_board_player_2
    global random_status_game_1
    global random_status_game_2
    global strike_counter

    random_status_game_1 = 1  # range_int(1, 2, "Игрок №1: Как стрелять (1 - руками, 2 - рандомно): ")
    random_status_game_2 = 1  # range_int(1, 2, "Игрок №2: Как стрелять (1 - руками, 2 - рандомно): ")
    strike_counter = 0

    ships_1 = MyShips(x, y)
    test_board = ships_1.generateBoard()
    ships_1.set_all_ships_cords()
    random_status_1 = 2  # range_int(1, 2, "Игрок №1: Как разместить корабли (1 - руками, 2 - рандомно): ")
    board_player_one, coords_1 = ships_1.choose_ship("Игрок №1", test_board, random_status_1)

    print_desk_gui(board_player_one, canv1)

    ships_2 = MyShips(x, y)
    test_board = ships_2.generateBoard()
    ships_2.set_all_ships_cords()
    random_status_2 = 2  # range_int(1, 2, "Игрок №2: Как разместить корабли (1 - руками, 2 - рандомно): ")
    board_player_two, coords_2 = ships_2.choose_ship("Игрок №2", test_board, random_status_2)

    print_desk_gui(board_player_two, canv1_win2)

    player_1 = LoseOrWin(x, y)
    player_1.win_score()
    player_2 = LoseOrWin(x, y)
    player_2.win_score()

    clean_board1 = Board(x, y)
    clean_board2 = Board(x, y)
    attack_board_player_1 = clean_board1.generateBoard()
    attack_board_player_2 = clean_board2.generateBoard()


def game_settings():
    pass


def exit_app():
    root.destroy()


def print_desk_gui(board, canv):
    for counter_row in range(1, 11):
        for counter_col in range(1, 11):
            for point in board[counter_row][counter_col]:
                if point == u'\u2588':  # корабль
                    canv.create_rectangle(20+(counter_col-1)*30, 20+(counter_row-1)*30, 50+(counter_col-1)*30, 50+(counter_row-1)*30, fill='#0008a1', outline="blue", tag="game_obj")
                elif point == u'\u2591':  # убитый корабль
                    canv.create_rectangle(20+(counter_col-1)*30, 20+(counter_row-1)*30, 50+(counter_col-1)*30, 50+(counter_row-1)*30, fill='#1d1f40', outline="#6500a3", tag="game_obj")
                elif point == u'\u2593':  # попали по кораблю
                    canv.create_rectangle(20+(counter_col-1)*30, 20+(counter_row-1)*30, 50+(counter_col-1)*30, 50+(counter_row-1)*30, fill='#750000', outline="red", tag="game_obj")
                elif point == "*":
                    canv.create_oval(30+(counter_col-1)*30, 30+(counter_row-1)*30, 40+(counter_col-1)*30, 40+(counter_row-1)*30, fill='#005', outline="blue", tag="game_obj")
                elif point == "X":
                    canv.create_oval(30+(counter_col-1)*30, 30+(counter_row-1)*30, 40+(counter_col-1)*30, 40+(counter_row-1)*30, fill='#4f7af0', outline="red", tag="game_obj")
    root.update()


def canvas_line(canv):  # Линии на досках
    for y in range(11):
        k = 30 * y
        canv.create_line(20 + k, 320, 20 + k, 20, width=1, fill="blue")

    for x in range(11):
        k = 30 * x
        canv.create_line(20, 20 + k, 320, 20 + k, width=1, fill="blue")


def canvas_coords_name(canv):
    for y in range(10):
        k = 30 * y
        canv.create_text(35 + k, 10, text=ascii_letters[y], fill="#888")
        canv.create_text(35 + k, 330, text=ascii_letters[y], fill="#888")

    for x in range(10):
        k = 30 * x
        canv.create_text(10, 35 + k, text=x+1, fill="#888")
        canv.create_text(330, 35 + k, text=x+1, fill="#888")


def canvas_clear(canv):
    canv.delete("game_obj")
    canv.config(bg='#001', cursor="target")

root = Tk()
root.title("Battleship 3.0 - 1 Игрок")
root.resizable(False,False)

main_menu = Menu(root)
root.configure(menu=main_menu)

label1 = Label(root, text="Твоя доска")
label1.grid(row=0, column=0)
label2 = Label(root, text="Доска соперника")
label2.grid(row=0, column=2)

canv1 = Canvas(root, width=340, height=340, bg='#001', cursor="boat")
canvas_line(canv1)
canvas_coords_name(canv1)
canv1.grid(row=1, column=0)
canv2 = Canvas(root, width=340, height=340, bg='#001', cursor="target")
canvas_line(canv2)
canvas_coords_name(canv2)
canv2.grid(row=1, column=2)

canv_separator = Canvas(root, width=50, height=10)
canv_separator.grid(row=3, column=1)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Новая игра", menu=first_item)
first_item.add_command(label="1 Игрок", command=game_for_one)
first_item.add_command(label="2 Игрока", command=game_for_two)
first_item.add_separator()
first_item.add_command(label="Выход", command=exit_app)

canv2.bind("<Button-1>", mouse_input)

root.mainloop()
