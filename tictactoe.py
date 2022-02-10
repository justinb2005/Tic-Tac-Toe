class Tic:
    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.remaining = ''

    def update_remaining(self,new):
        self.new = new
        self.remaining = self.remaining + self.new


    def print_board(self):
        print(str(self.board[0]) + ' | ' + str(self.board[1]) + ' | ' + str(self.board[2]))
        print('--+---+--')
        print(str(self.board[3]) + ' | ' + str(self.board[4]) + ' | ' + str(self.board[5]))
        print('--+---+--')
        print(str(self.board[6]) + ' | ' + str(self.board[7]) + ' | ' + str(self.board[8]))

    def make_move(self, move, turn, count=1, winner=False):
        self.move = move
        self.turn = turn
        self.count = count
        self.winner = winner
        print(self.count)


        if self.count >= 9 and self.winner == False:
            print('Draw')
            return

        if self.move not in '0123456789' or self.move in self.remaining:
            self.move = input(f'Player {self.turn} make a valid move: ')
            self.make_move(self.move, self.turn, self.count, self.winner)

        while self.count < 9 and self.winner == False:
            for spot in self.board:
                if spot == int(self.move):
                    self.board[spot] = self.turn
                    self.count += 1
                    self.print_board()
                    self.update_remaining(str(spot))

            if self.board[0] == self.board[1] == self.board[2]:
                print(f'Player {self.board[0]} wins!')
                self.winner = True
                break

            if self.board[0] == self.board[3] == self.board[6]:
                print(f'Player {self.board[0]} wins!')
                self.winner = True
                break
            if self.board[0] == self.board[4] == self.board[8]:
                print(f'Player {self.board[0]} wins!')
                self.winner = True
                break
            if self.board[3] == self.board[4] == self.board[5]:
                print(f'Player {self.board[3]} wins!')
                self.winner = True
                break
            if self.board[6] == self.board[7] == self.board[8]:
                print(f'Player {self.board[6]} wins!')
                self.winner = True
                break
            if self.board[1] == self.board[4] == self.board[7]:
                print(f'Player {self.board[1]} wins!')
                self.winner = True
                break
            if self.board[2] == self.board[5] == self.board[8]:
                print(f'Player {self.board[2]} wins!')
                self.winner = True
                break
            if self.board[2] == self.board[4] == self.board[6]:
                print(f'Player {self.board[2]} wins!')
                self.winner = True
                break
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.move = input(f'Player {self.turn} make your move: ')
            self.make_move(self.move, self.turn, self.count, self.winner)

    def start_game(self):
        self.turn = 'X'
        self.print_board()
        self.move = input(f'Player {self.turn} make your move: ')
        self.make_move(self.move, self.turn)
tic = Tic()
tic.start_game()