import numpy as np

dt = np.dtype([('type', np.unicode_), ('owner',np.int_)])

# Returns an array of threats if the arrangement of
# the pieces is a check, otherwise false
def isCheck(pieces, player):

    board = np.full((8,8), -1, dtype=dt)

    player_king = None
    player_white = player == 0

    for p in pieces:
        board[p['x'], p['y']]['type'] = p['piece']
        board[p['x'], p['y']]['owner'] = p['owner']
        if p['owner'] == player and p['piece'] == 'king':
            player_king = convert_to_point(p)


    threats = []

    moves = {'king': king_attacks, 'rook': rook_attacks, 'bishop': bishop_attacks, 'queen': queen_attacks,
             'knight': knight_attacks, 'pawn': pawn_attacks}

    for p in pieces:
        if p['owner'] == player:
            continue
        xy = convert_to_point(p)
        if moves[p['piece']](xy, player_king, board, player_white):
            threats.append(p)

    return threats


def convert_to_point(piece):
    return np.array([piece['x'], piece['y']])


def out_of_range(point):
    return point[0] < 0 or point[0] >= 8 or point[1] < 0 or point[1] >= 8


def nobody_block(start, end, step, board):
    while not out_of_range(start):
        start = start + step
        if np.array_equal(start, end):
            return True
        if board[tuple(start.tolist())]['owner'] != -1:
            return False
    return False


def king_attacks(self, enemy_king, board, player_white):
    return False


def rook_attacks(self, target, board, player_white):
    step = np.array([0, 0])
    if self[0] - target[0] == 0:
        step[1] = -1 if self[1] - target[1] > 0 else 1
    elif self[1] - target[1] == 0:
        step[0] = -1 if self[0] - target[0] > 0 else 1
    else:
        return False
    return nobody_block(self, target, step, board)


def bishop_attacks(self, target, board, player_white):
    step = np.array([0, 0])
    if abs(self[0] - target[0]) == abs(self[1] - target[1]):
        step[0] = -1 if self[0] - target[0] > 0 else 1
        step[1] = -1 if self[1] - target[1] > 0 else 1
    else:
        return False
    return nobody_block(self, target, step, board)


def queen_attacks(self, target, board, player_white):
    return rook_attacks(self, target, board, player_white) or bishop_attacks(self, target, board, player_white)


def knight_attacks(self, target, board, player_white):
    if abs(self[0] - target[0]) == 1 and abs(self[1] - target[1]) == 2:
        return True
    elif abs(self[0] - target[0]) == 2 and abs(self[1] - target[1]) == 1:
        return True
    return False


def pawn_attacks(self, enemy_king, board, player_white):

    if abs(self[0] - enemy_king[0]) == 1 and \
            self[1] - enemy_king[1] == -1 if player_white else 1:
        return True

    return False


# Returns true if the arrangement of the
# pieces is a check mate, otherwise false
def isMate(pieces, player):
    pass