#Выполненные доп. задания: №1(новые фигуры), №2(шашки), №5(откат ходов и шахматная нотация)


# перевод из шахматных координат в двумерный массив
def to_index(m):
    m = m.lower()
    if len(m) == 2 and m[1] in '12345678' and m[0] in 'abcdefgh':
        x = 8 - int(m[1])
        y = m[0]
    else:
        return False
    for i in range(8):
        if y == 'abcdefgh'[i]:
            y = i
            break
    return x, y


# проверка возможности походить выбранной фигурой на поле
def check_coord(x0, y0, player_number, fig, _board):
    if _board.board[x0][y0] == '·':
        print("Это пустое поле ", end="\n")
    if _board.board[x0][y0].isupper() != player_number:
        print("Сейчас ход соперника ", end="\n")
    f = None
    for i in fig: # поиск соответствующей фигуры в списке фигур
        if i.x0 == x0 and i.y0 == y0:
            f = i
    for i in range(8):
        for j in range(8):
            if f.hod_figur(i, j, _board): # проверка может ли данная фигура совершить такой ход
                return x0, y0

    print('Так нельзя ходить ')
    print()
    return None


#проверка поля, на которое мы хотим походить
def check_coord2(x0, y0, x, y, player_number, fig, _board):
    if _board.board[x][y] != '·' and _board.board[x][y].isupper() == player_number:
        print('Здесь уже стоит другая фигура ')
        print()
    for i in fig:
        if i.x0 == x0 and i.y0 == y0:
            if i.hod_figur(x, y, _board) == False:
                print('Так нельзя ходить ')
                print()
                return None
    return x0, y0, x, y


#Класс записи ходов фигур для возможности отмотать ходы
class MovesRecord:
    def __init__(self):
        self.records = []

    def add_record(self, start_field, end_field, figure):
        self.records.append([start_field, end_field, figure])

    def print_moves_record(self):
        print("Текущая запись ходов:")
        for i in self.records:
            print(i[0], "-", i[1], sep=" ")
        print()

    # метод отматывания ходов
    def move_back(self, _board):
        x0, y0 = to_index(self.records[-1][0])
        x, y = to_index(self.records[-1][1])
        _board.board[x0][y0] = _board.board[x][y]
        _board.board[x][y] = self.records[-1][2]
        self.records.pop()

# Далее идут классы фигур с методами проверки возможности хода фигуры
class Peshka:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:
            self.figure_name = "P"
        else:
            self.figure_name = "p"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board): # x0, y0 это то, где фигура находится в данный момент, а x и y - то, куда надо походить
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if self.y0 == y:
            if (self.x0 == 6 and x == 4 and _board.board[5][self.y0] == _board.board[4][
                self.y0] == '·' and self.player_number) or (
                    self.x0 == 1 and x == 3 and _board.board[2][self.y0] == _board.board[3][
                self.y0] == '·' and self.player_number == False):
                return True
            elif _board.board[x][y] == '·' and ((self.player_number == True and self.x0 - x == 1) or (
                    self.player_number == False and self.x0 - x == -1)):
                return True
        elif abs(y - self.y0) == 1 and _board.board[x][y] != '·' and (
                (self.player_number == True and self.x0 - x == 1) or (
                self.player_number == False and self.x0 - x == -1)):
            return True

class Kon:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:
            self.figure_name = "N"
        else:
            self.figure_name = "n"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if (x - self.x0) ** 2 + (y - self.y0) ** 2 == 5:
            return True
        else:
            return False


class Ladya:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:
            self.figure_name = "R"
        else:
            self.figure_name = "r"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if self.x0 == x:
            for i in range(min(self.y0, y) + 1, max(self.y0, y)):
                if _board.board[self.x0][i] != '·':
                    return False
            return True
        elif self.y0 == y:
            for i in range(min(self.x0, x) + 1, max(self.x0, x)):
                if _board.board[i][self.y0] != '·':
                    return False
            return True
        return False


class Slon:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:

            self.figure_name = "B"
        else:
            self.figure_name = "b"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if abs(self.x0 - x) == abs(self.y0 - y) and self.x0 - x != 0:
            step_y = int((y - self.y0) / abs(y - self.y0))
            step_x = int((x - self.x0) / abs(x - self.x0))
            j = self.x0 + step_x
            for i in range(self.y0 + step_y, y, step_y):
                if _board.board[j][i] != '·':
                    return False
                j += step_x
            return True
        return False


# Этот класс наследуется от ладьи и слона, потому что совмещает в себе их функционал
class Queen(Ladya, Slon):
    def __init__(self, x, y, player_number, _board):
        super().__init__(x, y, player_number, _board)
        if player_number:
            self.figure_name = "Q"
        else:
            self.figure_name = "q"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if Ladya.hod_figur(self, x, y, _board) or Slon.hod_figur(self, x, y, _board):
            return True
        else:
            return False


class King:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:
            self.figure_name = "K"
        else:
            self.figure_name = "k"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if abs(x - self.x0) <= 1 and abs(y - self.y0) <= 1:
            return True
        return False


# Классы новых фигур
# Первая фигура объединяет в себе слона и коня
class Figure1(Slon, Kon):
    def __init__(self, x, y, player_number, _board):
        super().__init__(x, y, player_number, _board)
        if player_number:
            self.figure_name = "W"
        else:
            self.figure_name = "w"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if Slon.hod_figur(self, x, y, _board) or Kon.hod_figur(self, x, y, _board):
            return True
        else:
            return False

#Вторая фигура объединяет короля и слона
class Figure2(King, Slon):
    def __init__(self, x, y, player_number, _board):
        super().__init__(x, y, player_number, _board)
        if player_number:
            self.figure_name = "U"
        else:
            self.figure_name = "u"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if King.hod_figur(self, x, y, _board) or Slon.hod_figur(self, x, y, _board):
            return True
        else:
            return False


#Конь, который ходит на 3 по горизонтали и на 3 по вертикали
class Figure3:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:
            self.figure_name = "I"
        else:
            self.figure_name = "i"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if (x - self.x0) ** 2 + (y - self.y0) ** 2 == 8:
            return True
        else:
            return False

#Класс шашечной фигуры
class Shashki:
    def __init__(self, x, y, player_number, _board):
        self.x0 = x
        self.y0 = y
        self.player_number = player_number
        if player_number:
            self.figure_name = "S"
        else:
            self.figure_name = "s"
        _board.board[self.x0][self.y0] = self.figure_name

    def hod_figur(self, x, y, _board):
        if _board.board[x][y] != '·' and _board.board[x][y].isupper() == self.player_number:
            return False
        if abs(x - self.x0) == 1 and abs(y - self.y0) == 1:
            return True
        else:
            return False


# Класс шахматной доски с методами печати поля и размещения фигур для обычных шахмат, шашек и шахмат с новыми фигурами
class Board:
    def __init__(self):
        self.board = []
        [self.board.append(["·"] * 8) for i in range(8)]

    def print_board(self):
        print(' | A B C D E F G H |')
        print('─────────────────────')
        for i in range(8):
            print(str(8 - i) + '│', end=' ')
            [print(self.board[i][j], end=' ') for j in range(8)]
            print('│' + str(8 - i))
        print('─────────────────────')
        print(' | A B C D E F G H |')
        print()

    def create_figur(_board):
        fig = {Ladya(0, 0, False, _board), Ladya(0, 7, False, _board), Ladya(7, 0, True, _board),
               Ladya(7, 7, True, _board),
               Kon(0, 1, False, _board), Kon(0, 6, False, _board), Kon(7, 1, True, _board),
               Kon(7, 6, True, _board),
               Slon(0, 2, False, _board), Slon(0, 5, False, _board), Slon(7, 2, True, _board),
               Slon(7, 5, True, _board),
               Queen(0, 3, False, _board), Queen(7, 3, True, _board), King(0, 4, False, _board),
               King(7, 4, True, _board),
               Peshka(1, 0, False, _board), Peshka(1, 1, False, _board), Peshka(1, 2, False, _board),
               Peshka(1, 3, False, _board), Peshka(1, 4, False, _board), Peshka(1, 5, False, _board),
               Peshka(1, 6, False, _board), Peshka(1, 7, False, _board),
               Peshka(6, 0, True, _board), Peshka(6, 1, True, _board), Peshka(6, 2, True, _board),
               Peshka(6, 3, True, _board), Peshka(6, 4, True, _board), Peshka(6, 5, True, _board),
               Peshka(6, 6, True, _board), Peshka(6, 7, True, _board)}
        return fig

    def create_new_figur(_board):
        fig = {Figure1(0, 0, False, _board), Figure1(0, 7, False, _board), Figure1(7, 0, True, _board),
               Figure1(7, 7, True, _board),
               Figure2(0, 1, False, _board), Figure2(0, 6, False, _board), Figure2(7, 1, True, _board),
               Figure2(7, 6, True, _board),
               Figure3(0, 2, False, _board), Figure3(0, 5, False, _board), Figure3(7, 2, True, _board),
               Figure3(7, 5, True, _board),
               Queen(0, 3, False, _board), Queen(7, 3, True, _board), King(0, 4, False, _board),
               King(7, 4, True, _board),
               Peshka(1, 0, False, _board), Peshka(1, 1, False, _board), Peshka(1, 2, False, _board),
               Peshka(1, 3, False, _board), Peshka(1, 4, False, _board), Peshka(1, 5, False, _board),
               Peshka(1, 6, False, _board), Peshka(1, 7, False, _board),
               Peshka(6, 0, True, _board), Peshka(6, 1, True, _board), Peshka(6, 2, True, _board),
               Peshka(6, 3, True, _board), Peshka(6, 4, True, _board), Peshka(6, 5, True, _board),
               Peshka(6, 6, True, _board), Peshka(6, 7, True, _board)}
        return fig

    def create_figur_shashki(_board):
        fig = {Shashki(7, 0, True, _board), Shashki(7, 2, True, _board), Shashki(7, 4, True, _board),
               Shashki(7, 6, True, _board),
               Shashki(6, 1, True, _board), Shashki(6, 3, True, _board), Shashki(6, 5, True, _board),
               Shashki(5, 0, True, _board), Shashki(5, 2, True, _board), Shashki(5, 4, True, _board),
               Shashki(5, 6, True, _board),
               Shashki(2, 1, False, _board), Shashki(2, 3, False, _board), Shashki(2, 5, False, _board),
               Shashki(1, 0, False, _board), Shashki(1, 2, False, _board), Shashki(1, 4, False, _board),
               Shashki(1, 6, False, _board),
               Shashki(0, 1, False, _board), Shashki(0, 3, False, _board), Shashki(0, 5, False, _board)}
        return fig


# Класс, отвечающий за ход самой игры
def play_game(_board, fig, moves_records):
    count = 1
    while True:
        _board.print_board()
        # Всегда спрашиваем хочет ли игрок отменить ход
        if count != 1:
            is_back = input("Хотите отменить предыдущий ход?(y/n) ")
            if is_back == "y":
                moves_records.move_back(_board)
                count -= 1
                continue
        player_number = count % 2
        # Поочередные ходы игроков
        if player_number:
            print('Ход заглавных: ', count, end="\n")
        else:
            print('Ход маленьких: ', count, end="\n")
        hod = input('Введите координаты фигуры: ')
        print()
        # Команда конца игры
        if hod == "стоп":
            break
        # Проверка на корректность введёных полей, если поле некорректно, то выбрасывает сообщение и предлагает походить снова
        try:
            start_field = hod[2:4]
            x0, y0 = to_index(hod[2:4])
            x0, y0 = check_coord(x0, y0, player_number, fig, _board)
        except:
            print('Неверный ход ', end="\n")
            continue
        try:
            end_field = hod[5:7]
            x, y = to_index(hod[5:7])
            x0, y0, x, y = check_coord2(x0, y0, x, y, player_number, fig, _board)
        except:
            print('Неверный ход ', end="\n")
            continue
        count += 1
        figure = _board.board[x][y]
        moves_records.add_record(start_field, end_field, figure)
        # Непосредственно переставление фигуры
        for i in fig:
            if i.x0 == x0 and i.y0 == y0:
                _board.board[x][y] = _board.board[x0][y0]
                _board.board[x0][y0] = '·'
                i.x0 = x
                i.y0 = y
        moves_records.print_moves_record()


def func():
    h = input('В какие шахматы сыграем? Обычные (1) или с новыми фигурами (2) или в шашки (3)? ')
    if h == '1':
        board = Board()
        fig = Board.create_figur(board)
        moves_record = MovesRecord()
        play_game(board, fig, moves_record)
    elif h == '2':
        board = Board()
        fig = Board.create_new_figur(board)
        moves_record = MovesRecord()
        play_game(board, fig, moves_record)
    elif h == '3':
        board = Board()
        fig = Board.create_figur_shashki(board)
        moves_record = MovesRecord()
        play_game(board, fig, moves_record)
    else:
        print("Некорректный номер", end="\n")
        func()

# Для игры нужно вводить ходы следующим образом: название_фигуры_на_поле поле_на_котором_стоит_фигура поле_на_которое_нужно_походить
# Например: P C2-C4
func()
