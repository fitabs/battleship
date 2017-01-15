# coding = utf-8


"""Проверка: допустимое значение числа"""
def range_int(low_value, higt_value, input_text, message = "Число вне диапазона"):

    variable = 0
    try:
        variable = int(input(input_text))
        """Проверка: допустимое значение числа"""
        if variable in range(low_value, higt_value + 1):
            return variable
        else:
            print(message)
            range_int(low_value, higt_value, input_text, message = "Число вне диапазона")
    except:
        print("Вы ввели не число!")
        range_int(low_value, higt_value, input_text, message = "Число вне диапазона")


class Board(object):
    """docstring for Board"""
    def __init__(self, x, y, alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.x = x
        self.y = y
        self.alpha = alpha

    def generateBoard(self):
        board = []
        count_line = 0
        alphabet = " ".join(self.alpha)
        board.append(["XX"] + [alphabet[:self.x * 2 - 1]])
        for line in range(self.y):
            count_line += 1
            board.append([str("{:02d}".format(count_line))] + ["O"] * self.x)
        return(board)

    def modificateBoard(self, board):
        modificate_board = []
        for line in range(self.y + 1):
            modificate_board.append(board[line] + [" "] * 10 + board[line])
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


class MyShips(Board):

    # def numbers_of_ships(self):
    #     ship_area_len = self.x * self.y * 0.2
    #     x = int("{0:.0f}".format(ship_area_len))
    #     print(ship_area_len)
    #     print(x)
    #     print(type(x))

    def draw_ship(self, board):
        ship_x = range_int(1, 20, "Введите Х корабля: ")
        ship_y = range_int(1, 20, "Введите Y корабля: ")
        board[ship_y][ship_x] = u'\u2588'  # Знак █ █ █ Unicode
        return board

    def draw_ship_random(self, board):
        ship_x = randint(1, self.x)
        ship_y = randint(1, self.y)
        board[ship_y][ship_x] = u'\u2588'  # Знак █ █ █ Unicode
        return board




class LoseOrWin(RabndomShip):
    """Нужен модуль - from random import randint"""

    def player_1(self):
        board = self.modificateBoard(self.generateBoard())
        ship_row = self.randRow() + 1 #Поправка на координаты строки 01 02 03
        ship_col = self.randCol() + 1 #Поправка на координаты колонны A B C
        return board, ship_row, ship_col

    def search_char(self, letter):
        self.letter = letter
        for char in range(len(self.alpha)):
            if self.alpha[char] == self.letter:
                return char + 1
                break
        print('Введен не верный символ, необходимо "A-{}"'.format(self.alpha[self.x]))


    def score(self, board, ship_row, ship_col):
        self.board = board
        self.ship_row = ship_row
        self.ship_col = ship_col
        self.win = 0

        coordinates = input("Введите координаты (Например B4): ")

        guess_alpha = coordinates[0]
        # while not guess_alpha.isalpha() or len(guess_alpha) != 1 or self.search_char(guess_alpha.upper()) > self.x:
        #     guess_alpha = input("Введите координаты - Колонна(A-{}): ".format(self.alpha[self.x - 1]))
        #     if len(guess_alpha) != 1:
        #         print('Введите один символ формата "A-Z"')
        #     elif not guess_alpha.isalpha():
        #         print('Это не буква! Введите что-нибудь формата "A-Z"')
        #     elif self.search_char(guess_alpha.upper()) > self.x:
        #         print("Допустимые координаты - Колонны(A-{}): ".format(self.alpha[self.x - 1]))
        guess_col = self.search_char(guess_alpha.upper())

        # guess_row = range_int(1, self.y, "Введите координаты - Строка(1-{}): ".format(self.y), "Допустимый номер строки 1 - {}".format(self.y))
        if len(coordinates) == 3:
            guess_row = int(coordinates[1] + coordinates[2])
        else:
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
    import os

    num_players = range_int(1, 2, "Введите количество игроков (1/2): ", "Могут играть только 1 или 2 игрока")

    x = 10 #range_int(5, 20, "Введите ширину доски: ", "Допустимая ширина доски 5 - 20")
    y = 10 #range_int(5, 20, "Введите высоту доски: ", "Допустимая высота доски 5 - 20")
    os.system('cls')

    print ("{:*^110}".format(" Игровая доска "))
    see_board = Board(x, y)
    test_board = see_board.modificateBoard(see_board.generateBoard())
    see_board.printBoard(test_board)

    ship = MyShips(x, y)
    ship.printBoard(ship.draw_ship_random(test_board))

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if num_players == 1:
        one_player = LoseOrWin(x, y)
        board, ship_row, ship_col = one_player.player_1()
        # print("Подсказка(-Колонна-) " + str(alpha[ship_col - 1]))
        # print("Подсказка(-Строка-) " + str(ship_row))


        turn = x * y
        batch = 0
        for batch in range(turn):
            game_score = one_player.score(board, ship_row, ship_col)
            if game_score == 1:
                print("Победа!")
                break

    elif num_players == 2:
        player_1 = LoseOrWin(x, y)
        board_1, ship_row_1, ship_col_1 = player_1.player_1()
        # print("Подсказка игроку 1(-Колонна-) " + str(alpha[ship_col_1 - 1]))
        # print("Подсказка игроку 1(-Строка-) " + str(ship_row_1))

        player_2 = LoseOrWin(x, y)
        board_2, ship_row_2, ship_col_2 = player_2.player_1()
        # print("Подсказка игроку 2(-Колонна-) " + str(alpha[ship_col_2 - 1]))
        # print("Подсказка игроку 2(-Строка-) " + str(ship_row_2))

        turn = x * y
        batch = 0
        for batch in range(turn):
            if batch % 2 == 0:
                print("\nХод игрока №1")
                game_score = player_1.score(board_1, ship_row_1, ship_col_1)
                if game_score == 1:
                    print("Игрок 1 победил!")
                    break
            else:
                print("\nХод игрока №2")
                game_score = player_2.score(board_2, ship_row_2, ship_col_2)
                if game_score == 1:
                    print("Игрок 2 победил!")
                    break


some_changes = 1
