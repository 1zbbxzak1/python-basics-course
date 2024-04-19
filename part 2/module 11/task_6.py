print('Задача 6. Крестики-нолики')

# Создайте программу, которая реализует игру «Крестики-нолики».


class Board:

    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def change_cell_state(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if not cell.occupied:
            cell.occupied = True
            cell.symbol = symbol
            return True
        else:
            return False

    def display_board(self):
        for i in range(0, 9, 3):
            print(
                f"{self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol}"
            )
            if i < 6:
                print("---------")

    def check_game_end(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                                [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for combo in winning_combinations:
            if (self.cells[combo[0]].symbol == self.cells[combo[1]].symbol ==
                    self.cells[combo[2]].symbol) and (
                        self.cells[combo[0]].symbol != ' '):
                return True

        return False


class Cell:

    def __init__(self, number):
        self.number = number
        self.occupied = False
        self.symbol = ' '


class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self, board):
        while True:
            try:
                move = int(
                    input(
                        f"{self.name}, введите номер ячейки, которую хотите отметить: "
                    ))
                if move in range(1, 10):
                    if board.change_cell_state(
                            move, 'X' if self.name == "Алиса" else 'O'):
                        return
                    else:
                        print(
                            "Эта ячейка уже занята. Пожалуйста, выберите другую."
                        )
                else:
                    print(
                        "Неверный ввод. Пожалуйста, введите число от 1 до 9.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")


class Game:

    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def play_turn(self, player):
        self.board.display_board()
        player.make_move(self.board)
        return self.board.check_game_end()

    def play_game(self):
        for _ in range(9):
            for player in self.players:
                if self.play_turn(player):
                    return True
        return False

    def start_game(self):
        while True:
            if self.play_game():
                print(
                    f"Поздравляем! {self.players[0].name if self.board.check_game_end() else self.players[1].name} победил(а)!"
                )
                self.players[0].wins += 1 if self.board.check_game_end() else 0
                self.players[1].wins += 1 if not self.board.check_game_end(
                ) else 0
            else:
                print("Ничья!")

            print(
                f"Счет: {self.players[0].name}: {self.players[0].wins}, {self.players[1].name}: {self.players[1].wins}"
            )

            while True:
                play_again = input("Хотите сыграть еще раз? (да/нет): ")
                if play_again.lower() == "да":
                    for cell in self.board.cells:
                        cell.occupied = False
                        cell.symbol = ' '
                    break
                elif play_again.lower() == "нет":
                    return
                else:
                    print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")


player1 = Player("Майк")
player2 = Player("Кларк")
game = Game(player1, player2)
game.start_game()

print()