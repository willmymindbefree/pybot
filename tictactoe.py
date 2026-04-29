class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        print('\n')
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
    
    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print('\n')
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def is_winner(self, player):
        # Check rows, columns, and diagonals
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def make_move(self, square, player):
        if self.board[square] == ' ':
            self.board[square] = player
            if self.is_winner(player):
                self.current_winner = player
            return True
        return False
    
    def empty_squares(self):
        return ' ' in self.board

def play():
    game = TicTacToe()
    players = ['X', 'O']
    current_player = 0
    
    print("Welcome to Tic Tac Toe!")
    game.print_board_nums()
    
    while game.empty_squares():
        player = players[current_player]
        
        while True:
            try:
                square = int(input(f"Player {player}'s turn! Pick a position (0-8): "))
                if 0 <= square <= 8 and game.make_move(square, player):
                    break
                else:
                    print("That position is taken or invalid!")
            except ValueError:
                print("Invalid input! Enter a number 0-8")
        
        game.print_board()
        
        if game.current_winner:
            print(f"Player {game.current_winner} won!")
            return
        
        if not game.empty_squares():
            print("It's a draw!")
            return
        
        current_player = 1 - current_player

if __name__ == "__main__":
    while True:
        play()
        if input("Play again? (yes/no): ").lower() != 'yes':
            break
