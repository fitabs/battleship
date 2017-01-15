#coding = utf-8

class InputINT(object):
    """Проверка: только нужное число"""
    def __init__(self, input_text):
        self.input_text = input_text
        self.variable = "not int"

    """Проверка: введено число"""
    def test_int(self):
        while type(self.variable) != int:
            try:
                self.variable = int(input(self.input_text))
            except:
                print("Вы ввели не число!")
        return self.variable

    """Проверка: допустимое значение числа"""
    def range_int(self, low_value, higt_value, message = "Число вне диапазона"):
        self.low_value = low_value
        self.higt_value = higt_value
        self.message = message

        x = self.low_value - 1

        while x not in range(self.low_value, self.higt_value + 1):
            try:
                x = int(input(self.input_text))
                if x < self.low_value or x > self.higt_value:
                    print(self.message)
            except:
                print("Вы ввели не число!")
        return x


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
        return board

    def printBoard(self, board):
        # self.board = board
        for row in board:
            print("{:^70}".format(" ".join(row)))


class RabndomShip(Board):
    """Нужен модуль - from random import randint"""
    # def myBoard(self):
    #     return(super(RabndomShip, self).generateBoard())

    def randRow(self):
        board = self.generateBoard()
        generatedRow = randint(0, len(board) - 2)
        return generatedRow

    def randCol(self):
        board = self.generateBoard()
        generatedCol = randint(0, len(board[1]) - 2)
        return generatedCol


class LoseOrWin(RabndomShip, InputINT):
    """Нужен модуль - from random import randint"""
    def player_1(self):
        board = self.generateBoard()
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
        
        guess_alpha = "00"
        while not guess_alpha.isalpha() or len(guess_alpha) != 1 or self.search_char(guess_alpha.upper()) > self.x:
            guess_alpha = input("Введите координаты - Колонна(A-{}): ".format(self.alpha[self.x - 1]))
            if len(guess_alpha) != 1:
                print('Введите один символ формата "A-Z"')
            elif not guess_alpha.isalpha():
                print('Это не буква! Введите что-нибудь формата "A-Z"')
            elif self.search_char(guess_alpha.upper()) > self.x:
                print("Допустимые координаты - Колонны(A-{}): ".format(self.alpha[self.x - 1]))
        guess_col = self.search_char(guess_alpha.upper())

        guess_row = InputINT("Введите координаты - Строка(1-{}): ".format(self.y))
        guess_row = guess_row.range_int(1, self.y, "Допустимый номер строки 1 - {}".format(self.y))

        if guess_row == self.ship_row and guess_col == self.ship_col:
            print ("{:*^70}".format(" Ты выиграл! "))
            board[guess_row][guess_col] = "*"
            self.win += 1
        else:
            if (guess_row < 0 or guess_row > self.x) or (guess_col < 0 or guess_col > self.y):
                print ("{:*^70}".format(" Oops, введены координаты за пределами доски. "))
            elif(board[guess_row][guess_col] == "X"):
                print ("{:*^70}".format(" Будь внимательнее! Ты уже стрелял по этой точке. "))
            else:
                print ("{:*^70}".format(" Ты промазал! "))
                board[guess_row][guess_col] = "X"
        self.printBoard(board)
        return self.win 

#####################################################################################################################################################################

if __name__ == '__main__':
              
    from random import randint

    num_players = InputINT("Введите количество игроков (1/2): ")
    num_players = num_players.range_int(1, 2, "Могут играть только 1 или 2 игрока")

    x = InputINT("Введите ширину доски: ")
    x = x.range_int(1, 23, "Допустимая ширина доски не более 26")
    y = InputINT("Введите высоту доски: ")
    y = y.range_int(1, 99, "Допустимая высота доски не более 99")

    alpha = "ABCDEFGHIKLMNOPQRSTVXYZ"

    if num_players == 1:
        one_player = LoseOrWin(x, y)
        board, ship_row, ship_col = one_player.player_1()
        print("Подсказка(-Колонна-) " + str(alpha[ship_col - 1]))
        print("Подсказка(-Строка-) " + str(ship_row))


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
        print("Подсказка игроку 1(-Колонна-) " + str(alpha[ship_col_1 - 1]))
        print("Подсказка игроку 1(-Строка-) " + str(ship_row_1))

        player_2 = LoseOrWin(x, y)
        board_2, ship_row_2, ship_col_2 = player_2.player_1()
        print("Подсказка игроку 2(-Колонна-) " + str(alpha[ship_col_2 - 1]))
        print("Подсказка игроку 2(-Строка-) " + str(ship_row_2))
        
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


