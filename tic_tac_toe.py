from random import randint

#------------------------------------------------class definitions



class Board():
    """Board on which tic tac toe is played"""

    def __init__(self, cells={}, finished=False, winner=None):
        self.cells = cells
        self.finished = finished
        self.winner = winner

    def check_win(self):
        """
        Checks the board for win states (3 in a row, 3 in a column, diagonals, or tie.
        On a win, update winner attribute to the contents of one of the winning cells ('x' or 'o')
        """

        for i in ['1', '2', '3']:
            #check rows
            if self.cells[i + '-1'].contents != '-' and self.cells[i + '-1'].contents == self.cells[i + '-2'].contents == self.cells[i + '-3'].contents:
                self.finished = True
                self.winner = self.cells[i + '-1'].contents

            #check columns
            if self.cells['1-' + i].contents != '-' and self.cells['1-' + i].contents == self.cells['2-' + i].contents == self.cells['3-' + i].contents:
                self.finished = True
                self.winner = self.cells['1-' + i].contents
        
        #check diagonals
        if (
            self.cells['2-2'].contents != '-' and
            (
                self.cells['2-2'].contents == self.cells['1-1'].contents == self.cells['3-3'].contents
                or
                self.cells['2-2'].contents == self.cells['1-3'].contents == self.cells['3-1'].contents
            )
        ):
            self.finished = True
            self.winner = self.cells['2-2'].contents

        #check for tie
        if '-' not in [cell.contents for cell in self.cells.values()]:
            self.finished = True

    def __repr__(self):

        board_repr = ""

        for r in ['1', '2', '3']:
            for c in ['1', '2', '3']:
                board_repr += f'[{self.cells[r + "-" + c].contents}]'
            board_repr += '\n'

        return board_repr


class Cell():
    """One of nine cells in the tic tac toe board"""

    def __init__(self, row, column, contents='-'):
        self.row = row
        self.column = column
        self.contents = contents

    def update(self, contents):
        """Changes content of the cell"""
        self.contents = contents

    def __repr__(self):
        return f'<Cell obj {self.row}-{self.column}: {self.contents}>'


class Player():

    def __init__(self, turn_mod=None, marker=None):
        self.turn_mod = turn_mod
        self.marker = marker

    def choose_cell(self):
        """Prompts player for coordinates of their desired cell."""
        r = input('Choose a row: ')
        c = input('Choose a column: ')
        return {
            'row': r,
            'column': c,
            'marker': self.marker
        }

    def __repr__(self):
        return f'<Player {self.marker}>'



#------------------------------------------------setup



#instantiate board as Board object
board = Board()

#populate board.cells with instances of Cell class
for r in ['1', '2', '3']:
    for c in ['1', '2', '3']:
        key = r + '-' + c
        board.cells[key] = Cell(row=r, column=c)

#instantiate players
player_x = Player(marker='x')
player_o = Player(marker='o')

#set up turn order
def turn_order():
    print('Let\'s see who goes first.')
    """Randomly assigns turn order and updates players' turn_mod attributes"""
    if randint(0, 1) == 1:
        player_x.turn_mod, player_o.turn_mod = 0, 1
        print('Player X will go first.')
    else:
        player_x.turn_mod, player_o.turn_mod = 1, 0
        print('Player O will go first.')

#initialize turn count
turn_count = 0



#------------------------------------------------exposition or other



#intro to tic tac toe
def intro():
    """Introduction and exposition to the game."""
    print('Welcome to tic tac toe!')
    print('Xs or Os, 3 in a row! Fill them in and then you win!')


#function to handle turn
def handle_choice(cell: dict):
    """Takes in dict containing player choice info and updates the specified cell in the board"""
    key = cell['row'] + '-' + cell['column']
    board.cells[key].update(cell['marker'])


def outro():
    """Prints final board state and announces winner or tie"""
    print(board)
    if board.winner:
        print(f'Player {board.winner.upper()} wins!')
    else:
        print('You must both be tic tac toe experts, because you tied.')



#------------------------------------------------gameplay



intro()
turn_order()

#while game is still going
while board.finished == False:

    #show board state
    print(board)

    #if it's X's turn, announce this, prompt for cell choice, update cell
    if turn_count % 2 == player_x.turn_mod:
        print('Player X, please choose your row and column.')
        handle_choice(player_x.choose_cell())
    #if it's O's turn, do the same for O
    else:
        print('Player O, please choose your row and column.')
        handle_choice(player_o.choose_cell())

    board.check_win()
    turn_count += 1

outro()