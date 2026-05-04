"""
    tic_tac_toe.py

    A Python version of Tic-Tac-Toe that saves the game to a JSON file.
"""
import json


class Player:
    """Represents a player in Tictactoe."""

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
    
    def __str__(self):
        return f"{self.name}({self.symbol})."

class TicTacToe:
    """Tic-Tac-Toe game using a list."""

    def __init__(self, player1: Player, player2: Player):
        self.board: list = [' '] * 9
        self.players = [player1, player2]
        self.player_index = 0
        self.move_count = 0
        self.filename = "tictac_save.json"
        # Numpad to index.
        self.position_map = {
            7: 0, 8: 1, 9: 2,
            4: 3, 5: 4, 6: 5,
            1: 6, 2: 7, 3: 8,
        }

    def print_board(self):
        """Prints the current board."""
        for i in range(0, 9, 3):
            print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('---+---+---')
        print()

    def print_numpad_reference(self):
        """Shows corresponding numbers to cells of the board."""
        print()
        print('  7  8  9')
        print('  4  5  6')
        print('  1  2  3\n')
    
    def make_move(self, num: int) -> bool:
        """Attempt to make a move and returns True if it is successful."""
        if num not in self.position_map:
            print('Number is not valid!')
            return False
    
        index = self.position_map[num]

        if self.board[index] != ' ':
            print('That cell is occupied!')
            return False
    
        current_player = self.players[self.player_index]
        self.board[index] = current_player.symbol
        self.move_count += 1
        return True

    def check_winner(self) -> Player | None:
        """Checks for a win condition being met."""
        char = self.players[self.player_index].symbol
        winning_combos = [
            (0,1,2), (3,4,5), (6,7,8),  # Rows
            (0,3,6), (1,4,7), (2,5,8),  # Columns
            (0,4,8), (2,4,6)            # Diagonal
        ]

        for combo in winning_combos:
            if all(self.board[index] == char for index in combo):
                return self.players[self.player_index].name
        return None

    def is_draw(self) -> bool:
        """Check for a draw."""
        return self.move_count == 9 and self.check_winner() is None

    def save_game(self, filename=None):
        """Save game progress with JSON."""
        if filename is None:
            filename = self.filename

        game_state = {
            'board': self.board,
            'player1': {'name': self.players[0].name, 'symbol': self.players[0].symbol},
            'player2': {'name': self.players[1].name, 'symbol': self.players[1].symbol},
            'current_player_index': self.player_index,
            'move_count': self.move_count
        }

        try:
            with open(filename, 'w') as f:
                json.dump(game_state, f)
            print(f'\nGame saved to {filename}')
        except Exception as e:
            print(f'\nFailed to save because of {e}.')

    def load_game(self, filename=None) -> bool:
        """Load game from JSON or return False."""
        if filename is None:
            filename = self.filename
        
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)

            self.board = game_state['board']
            self.players[0] = Player(game_state['player1']['name'], game_state['player1']['symbol'])
            self.players[1] = Player(game_state['player2']['name'], game_state['player2']['symbol'])
            self.player_index = game_state['current_player_index']
            self.move_count = game_state['move_count']
            print(f"\nGame loaded from {filename}")
            return True
        except FileNotFoundError:
            print(f"\nSave file {filename} not found!\n")
            return False

    def play(self):
        """Game loop with save on Ctrl+C."""

        self.print_numpad_reference()

        try:
            while True:
                self.print_board()
                current_player_name = self.players[self.player_index].name
                current_player_symbol = self.players[self.player_index].symbol

                print(f"It is {current_player_name}'s turn.")
                print('Input 1-9 to draw in the boxes.')
                try:
                    num = int(input(f"{current_player_symbol}: "))
                    print()
                except ValueError:
                    print('Input is not valid!')
                    continue
                
                if self.make_move(num):
                    winner = self.check_winner()
                    if winner:
                        self.print_board()
                        print(f'{winner} won!')
                        break
                    
                    if self.is_draw():
                        self.print_board()
                        print('Oops, the game is a draw!')
                        break
                    
                    self.player_index = 1 - self.player_index
                else:
                    print('Try again.\n')

        except KeyboardInterrupt:
            self.save_game()
            print(f'Game saved successfully to {self.filename}.')


def get_player(player_num: int, taken_symbol: str = None) -> Player:
    """
        Player name and symbol is input.
        To-do: Add functionality to input a name along with a symbol using .split.
    """
    name = input(f'Enter player {player_num} name: ').strip()
    while not name:                
        name = input('Name cannot be blank!').strip()

    while True:
        symbol = input(f'{name} Character: ').strip()
        if not symbol:
            print('Symbol cannot be blank!')
            continue
        if len(symbol) > 1:
            print('Functionality for >1 character symbols is being worked on.')
            continue
        if taken_symbol and symbol == taken_symbol:
            print('That is taken already!')
            continue
        break

    return Player(name, symbol)


def get_player_info() -> tuple[Player, Player]:
    """Call function for 2 players."""
    print('Welcome to Tic-Tac-Toe!')
    p1 = get_player(1)
    p2 = get_player(2, p1.symbol)
    return p1, p2


def main():
    """Main function with game save/load logic."""
    game = TicTacToe(Player("", ""), Player("", ""))
    try:
        if not game.load_game():
            print()
            game.print_board()   # Show empty board
            player1, player2 = get_player_info()
            game = TicTacToe(player1, player2)
        game.play()
        
    # Fixed crash caused by Ctrl+C when names were not input.
    except KeyboardInterrupt:
        if game.players[0].name and game.players[1].name:
            game.save_game()


if __name__ == '__main__':
    main()
