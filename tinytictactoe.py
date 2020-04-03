import itertools

def tictactoe():
    active_player = 'X'
    board = [['.' for j in range(3)] for i in range(3)]
    while True:
        if active_player == 'X':
            for row in board: print(' '.join(row))
            move = get_player_move(board)
        else:
            move, evaluation = get_best_move(board, active_player)
        
        board[move[0]][move[1]] = active_player
        winner = get_winner(board)
        if winner != None:
            print('Game Over! {} Wins'.format(winner))
            break
        elif len(get_open_moves(board)) == 0:
            print('Game Over! Nobody Wins')
            break
        active_player = 'O' if active_player == 'X' else 'X'
    return winner

def get_open_moves(board):
    open_moves = []
    for row_num, row in enumerate(board):
        for col_num, cell in enumerate(row):
            if cell == '.':
                open_moves.append((row_num, col_num))
    return open_moves

def get_player_move(board):
    open_moves = get_open_moves(board)
    while True:
        try:
            square = int(input('Input a move (1-9):  ')) - 1
            move = (square // 3, square % 3)
            if move in open_moves:
                return move
        except ValueError:
            continue

cache = {'X':{}, 'O':{}}
def get_best_move(board, active_player):
    winner = get_winner(board)
    if winner is None:
        try:
            return cache[active_player][str(board)]
        except KeyError:
            pass

        moves = get_open_moves(board)
        if not moves:
            return (None, 0)

        scores = []
        for move in moves:
            new_board = [[cell for cell in row] for row in board]
            new_board[move[0]][move[1]] = active_player
            next_player = 'X' if active_player == 'O' else 'O'
            outcome = get_best_move(new_board, next_player)
            scores.append(-outcome[1])
            cache[next_player][str(new_board)] = outcome
        return max(zip(moves, scores), key=lambda x: x[1])
    elif winner == active_player:
        return (None, 1)
    else:
        return (None, -1)

def get_winner(board):
    cols = zip(*board)
    forward_diag = [[board[i][i] for i in range(3)]]
    backward_diag = [[row[-i-1] for i, row in enumerate(board)]]

    for row in itertools.chain(board, cols, forward_diag, backward_diag):
        if len(set(row)) == 1 and '.' not in row:
            return row[0]

if __name__ == '__main__':
    tictactoe()
