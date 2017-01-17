# coding = utf-8


"""Проверка: допустимое значение числа"""
def range_int(low_value, higt_value, input_text, message = "Число вне диапазона"):

    try:
        variable = int(input(input_text))
        """Проверка: допустимое значение числа"""
        if variable in range(low_value, higt_value + 1):
            return variable
        else:
            print(message)
            range_int(low_value, higt_value, input_text, message="Число вне диапазона")
    except:
        print("Вы ввели не число!")
        range_int(low_value, higt_value, input_text, message="Число вне диапазона")


def search_char(letter):
    for char in range(26):
        if ascii_letters[char] == letter:
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
            modificate_board.append(board_1[line] + [" "] * 10 + board_2[line])
        return(modificate_board)

    def printBoard(self, board):
        print("{:*^55}".format(" Твоя доска. ") + "{:*^55}".format(" Доска соперника. "))
        for row in board:
            print("{:^110}".format(" ".join(row)))


class RabndomShip(Board):
    """Нужен модуль - from random import randint"""

    def randRow(self):
        board = self.generateBoard()
        generatedRow = randint(0, len(board) - 2)
        return generatedRow

    def randCol(self):
        board = self.generateBoard()
        generatedCol = randint(0, len(board[1]) - 2)
        return generatedCol


class MyShips(object):


    def choose_ship(self, board):
        self.board = board
        all_ships = {1:4, 2:3, 3:2, 4:1}  # 1:4 == 1 палубный корабль 4 штук
        for x in range(10):
            type = int(input("Количество палуб коробля (1-4) "))
            all_ships[type] -= 1
            for x in range(type):
                self.printBoard(self.draw_ship(board))


    def draw_ship(self, board):
        ship_x = range_int(1, 20, "Введите Х корабля: ")
        ship_y = range_int(1, 20, "Введите Y корабля: ")
        if board[ship_y][ship_x] == "O":
        # if board[ship_y][ship_x] == "O" and \
        #                 board[ship_y-1][ship_x] == "O" and board[ship_y+1][ship_x] == "O" and \
        #                 board[ship_y][ship_x-1] == "O" and board[ship_y][ship_x+1] == "O":
            board[ship_y][ship_x] = u'\u2588'  # Знак █ █ █ Unicode
        return board


class LoseOrWin(RabndomShip):
    """Нужен модуль - from random import randint"""


    def score(self, board_my, board_comp):
        self.win = 0

        coordinates = input("Введите координаты (Например B-4): ").split('-')
        guess_alpha = coordinates[0]
        guess_col = self.search_char(guess_alpha.lower())
        guess_row = int(coordinates[1])
        os.system('cls')


        if guess_row == self.ship_row and guess_col == self.ship_col:
            print ("{:*^110}".format(" Ты выиграл! "))
            board[guess_row][guess_col + 11 + self.x] = "*"
            self.win += 1
        else:
            if (guess_row < 0 or guess_row > self.x * 2 + 10) or (guess_col < 0 or guess_col > self.y):
                print ("{:*^110}".format(" Oops, введены координаты за пределами доски. "))
            elif(board[guess_row][guess_col + 11 + self.x] == "X"):
                print ("{:*^110}".format(" Будь внимательнее! Ты уже стрелял по этой точке. "))
            else:
                print ("{:*^110}".format(" Ты промазал! "))
                board[guess_row][guess_col + 11 + self.x] = "X"
        self.printBoard(board)
        return self.win

###################################################################################################################

if __name__ == '__main__':

    from random import randint
    from string import ascii_letters
    import os

    x = 10 # range_int(5, 20, "Введите ширину доски: ", "Допустимая ширина доски 5 - 20")
    y = 10 # range_int(5, 20, "Введите высоту доски: ", "Допустимая высота доски 5 - 20")

    print ("{:*^110}".format(" Игровая доска "))
    player_one = Board(x, y)
    test_board = player_one.modificateBoard(player_one.generateBoard())
    player_one.printBoard(test_board)

    ship = MyShips()
    board_player_one = ship.choose_ship(test_board)

    print("{:*^110}".format(" Игровая доска "))
    player_two = Board(x, y)
    test_board = player_two.modificateBoard(player_two.generateBoard())
    player_two.printBoard(test_board)

    ship = MyShips()
    board_player_two = ship.choose_ship(test_board)

    player_1 = LoseOrWin(x, y)
    player_2 = LoseOrWin(x, y)

    turn = x * y
    batch = 0
    for batch in range(turn):
        if batch % 2 == 0:
            print("\nХод игрока №1")
            game_score = player_1.score(board_player_one, board_player_two)
            if game_score == 1:
                print("Игрок 1 победил!")
                break
        else:
            print("\nХод игрока №2")
            game_score = player_2.score(board_player_two, board_player_one)
            if game_score == 1:
                print("Игрок 2 победил!")
                break

