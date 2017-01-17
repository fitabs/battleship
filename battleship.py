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


def full_data():
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    second = str(datetime.now().second)
    full_data = year + '-' + month + '-' + day + '_' + hour + '-' + minute + '-' + second
    return full_data


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

    def printBoard(self, board):
        print("{:*^55}".format(" Твоя доска. ") + "{:*^55}".format(" Доска соперника. "))
        for row in board:
            print("{:^110}".format(" ".join(row)))


class MyShips(Board):


    def choose_ship(self, board):
        self.board = board
        all_ships = {1:4, 2:3, 3:2, 4:1}  # 1:4 == 1 палубный корабль 4 штук
        num_ships = 1
        for x in range(num_ships):
            type = int(input("Количество палуб коробля (1-4) "))
            if all_ships[type] > 0:
                for x in range(type):
                    self.printBoard(self.draw_ship(board))
                    all_ships[type] -= 1
            else:
                print("Кораблей данного типа больше нет")
                print(all_ships)
                num_ships += 1 # чот ничо не пашет=\
        return board


    def draw_ship(self, board):
        ship_x = range_int(1, 20, "Введите Х корабля: ")
        ship_y = range_int(1, 20, "Введите Y корабля: ")
        if board[ship_y][ship_x] == "O":
        # if board[ship_y][ship_x] == "O" and \
        #                 board[ship_y-1][ship_x] == "O" and board[ship_y+1][ship_x] == "O" and \
        #                 board[ship_y][ship_x-1] == "O" and board[ship_y][ship_x+1] == "O":
            board[ship_y][ship_x] = u'\u2588'  # Знак █ █ █ Unicode
        return board


class LoseOrWin(Board):
    """Нужен модуль - from random import randint"""


    def score(self, show_my_board, show_comp_board, hide_comp_board):
        self.show_my_board = show_my_board
        self.show_comp_board = show_comp_board

        win = 0
        marker = ''

        coordinates = input("Введите координаты (Например B-4): ").split('-')
        guess_alpha = coordinates[0]
        guess_col = search_char(guess_alpha.lower())
        guess_row = int(coordinates[1])
        os.system('cls')


        if hide_comp_board[guess_row][guess_col] == u'\u2588':
            print ("{:*^110}".format(" Ты попал! "))
            show_comp_board[guess_row][guess_col] = "*"
            hide_comp_board[guess_row][guess_col] = "*"
            marker = "*"
            win += 1
        else:
            if (guess_row < 0 or guess_row > len(show_my_board)) or (guess_col < 0 or guess_col > len(show_my_board)):
                print ("{:*^110}".format(" Oops, введены координаты за пределами доски. "))
            elif show_comp_board[guess_row][guess_col] == "X" or show_comp_board[guess_row][guess_col] == "*":
                print ("{:*^110}".format(" Будь внимательнее! Ты уже стрелял по этой точке. "))
                marker = "X"
            else:
                print ("{:*^110}".format(" Ты промазал! "))
                show_comp_board[guess_row][guess_col] = "X"
                hide_comp_board[guess_row][guess_col] = "X"
                marker = "X"
        board = self.modificateBoard(show_my_board, show_comp_board)
        self.printBoard(board)
        return win, hide_comp_board

###################################################################################################################

if __name__ == '__main__':

    from random import randint
    from string import ascii_letters
    from datetime import datetime
    import openpyxl
    import os

    x = 10 # range_int(5, 20, "Введите ширину доски: ", "Допустимая ширина доски 5 - 20")
    y = 10 # range_int(5, 20, "Введите высоту доски: ", "Допустимая высота доски 5 - 20")

    print ("{:*^110}".format(" Игровая доска "))
    player_one = Board(x, y)
    test_board = player_one.generateBoard()
    for row in test_board:
        print("{:^110}".format(" ".join(row)))
    ship = MyShips(x, y)
    board_player_one = ship.choose_ship(test_board)

    # excel = openpyxl.load_workbook('./data/start.xlsx')
    # sheet = excel['Лист1']
    #
    # for row in openpyxl.compat.range(1, 11):
    #     for col in openpyxl.compat.range(1, 11):
    #         sheet.cell(column=col+1, row=row+2, value=test_board[row][col])
    #
    # excel.save('./data/' + full_data() + '.xlsx')

    print("{:*^110}".format(" Игровая доска "))
    player_two = Board(x, y)
    test_board = player_two.generateBoard()
    for row in test_board:
        print("{:^110}".format(" ".join(row)))
    ship = MyShips(x, y)
    board_player_two = ship.choose_ship(test_board)


    attack_board_player_1 = player_one.generateBoard()
    attack_board_player_2 = player_two.generateBoard()


    player_1 = LoseOrWin(x, y)
    player_2 = LoseOrWin(x, y)

    turn = x * y
    batch = 0
    for batch in range(turn):
        board_player_one = board_player_one
        board_player_two = board_player_two

        if batch % 2 == 0:
            print("\nХод игрока №1")
            game_score, board_player_two = player_1.score(board_player_one, attack_board_player_1, board_player_two)
            if game_score == 10:
                print("Игрок 1 победил!")
                break
        else:
            print("\nХод игрока №2")
            game_score, board_player_one = player_2.score(board_player_two, attack_board_player_2, board_player_one)
            if game_score == 10:
                print("Игрок 2 победил!")
                break

