class NoughtsAndCrosses:
    def __init__(self):
        self.player_1 = "X"
        self.player_2 = "O"
        self.grade = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = self.player_1
        self.move_history = []

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def perform_action(self, action):
        return action.execute(self)

class PrintGrade:
    def execute(self, game):
        print("     0     1     2")
        print("   _________________ ")
        for i, row in enumerate(game.grade):
            print(f"  |     |     |     |")
            print(f"{i} |  {row[0]}  |  {row[1]}  |  {row[2]}  |")
            print(f"  |_____|_____|_____|")
        print()

class MakeMove:
    def execute(self, game):
        print(f"{game.current_player}'s turn")
        while True:
            try:
                row = int(input("Enter the row: "))
                col = int(input("Enter the column: "))
                if (0 <= row <= 2) and (0 <= col <= 2):
                    if game.grade[row][col] == " ":
                        game.grade[row][col] = game.current_player
                        game.move_history.append((row, col))
                        game.switch_player()
                        break
                    else:
                        print("That spot is already taken. Try again.\n")
                else:
                    print("Invalid input! Row and column must be between 0 and 2.\n")
            except ValueError:
                print("Please enter valid integers for row and column.\n")

class CheckWinner:
    def execute(self, game):
        # checking rows
        for row in game.grade:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        # checking columns
        for c in range(3):
            if game.grade[0][c] == game.grade[1][c] == game.grade[2][c] != " ":
                return game.grade[0][c]
        # checking diagonals
        if game.grade[0][0] == game.grade[1][1] == game.grade[2][2] != " ":
            return game.grade[0][0]
        if game.grade[2][0] == game.grade[1][1] == game.grade[0][2] != " ":
            return game.grade[2][0]
        # checking draw
        if all(square != " " for row in game.grade for square in row):
            return "Draw"
        return None

class UndoMove:
    def execute(self, game):
        if not game.move_history:
            print("No moves to undo.")
            return
        row, col = game.move_history.pop()
        game.grade[row][col] = " "
        game.switch_player()
        print("Last move undone.")

def main():
    game = NoughtsAndCrosses()
    winner = None
    while winner is None:
        game.perform_action(PrintGrade())
        action = input("Enter 'm' to make a move or 'u' to undo the last move: ").strip().lower()
        if action == 'm':
            game.perform_action(MakeMove())
        elif action == 'u':
            game.perform_action(UndoMove())
        else:
            print("Invalid input.")
            continue
        winner = game.perform_action(CheckWinner())
    game.perform_action(PrintGrade())
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"The winner is {winner}!")

main()
