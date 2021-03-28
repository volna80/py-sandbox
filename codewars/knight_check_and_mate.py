import numpy as np

dt = np.dtype([('type', '<U5'), ('owner', np.int_)])

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


#return True if a cell is empty
def is_empty(board, xy):
    return board[xy[0], xy[1]]['owner'] == -1


def is_not_empty(board, xy):
    return not is_empty(board, xy)


def nobody_block(start, end, step, board):
    while not out_of_range(start):
        start = start + step
        if np.array_equal(start, end):
            return True
        if is_not_empty(board, start):
            return False
    return False


def king_attacks(self, enemy_king, board, player_white):
    if abs(self[0] - enemy_king[0]) <= 1 and abs(self[1] - enemy_king[1]) <=1:
        return True

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
            self[1] - enemy_king[1] == (-1 if player_white else 1):
        return True

    return False


# Returns true if the arrangement of the
# pieces is a check mate, otherwise false
def isMate(pieces, player):

    pieces = pieces.copy()

    if len(isCheck(pieces, player)) == 0:
        return False

    board = np.full((8, 8), -1, dtype=dt)
    en_passant = None

    for p in pieces:
        board[p['x'], p['y']]['type'] = p['piece']
        board[p['x'], p['y']]['owner'] = p['owner']
        if p['piece'] == 'pawn' and p.get('prevX') is not None:
            en_passant = p

    moves = {'king': king_move, 'rook': rook_move, 'bishop': bishop_move, 'queen': queen_move,
             'knight': knight_move, 'pawn': pawn_move}

    for i in range(len(pieces)):
        p = pieces[i]
        if p['owner'] != player:
            continue
        xy = convert_to_point(p)
        if not moves[p['piece']](p.copy(), xy, pieces[:i] + pieces[i+1:], player, board, en_passant):
            return False

    return True

# True if there is no move which save a king from a check
# Otherwise false
def king_move(self, xy, pieces, player, board, en_passant):
    return king_or_knight_move(self, xy, pieces, player, board, [np.array([1,-1]), np.array([1,0]), np.array([1,-1]),
                np.array([-1,-1]), np.array([-1,0]), np.array([-1,1]),
                np.array([0,1]), np.array([0,-1])])


def king_or_knight_move(self, xy, pieces, player, board, steps):
    for dxy in steps:
        newxy = xy + dxy
        if out_of_range(newxy):
            continue
        if board[newxy[0], newxy[1]]['owner'] == player:
            continue
        elif is_not_empty(board, newxy):
            #attack
            pieces2 = pieces.copy()
            for i in range(len(pieces2)):
                if pieces2[i]['x'] == newxy[0] and pieces2[i]['y'] == newxy[1]:
                    pieces2.remove(pieces2[i])
                    break

            self['x'] = newxy[0]
            self['y'] = newxy[1]
            if len(isCheck(pieces2 + [self], player)) == 0:
                return False
        else:
            self['x'] = newxy[0]
            self['y'] = newxy[1]
            if len(isCheck(pieces + [self], player)) == 0:
                return False

    return True

def rook_or_bishop_move(self, xy, pieces, player, board, steps):
    for dxy in steps:
        newxy = xy
        while True:
            newxy = newxy + dxy
            if out_of_range(newxy):
                break
            if board[newxy[0], newxy[1]]['owner'] == player:
                break
            elif is_not_empty(board, newxy):
                # attack
                pieces2 = pieces.copy()
                for i in range(len(pieces2)):
                    if pieces2[i]['x'] == newxy[0] and pieces2[i]['y'] == newxy[1]:
                        pieces2.remove(pieces2[i])
                        break
                self['x'] = newxy[0]
                self['y'] = newxy[1]
                if len(isCheck(pieces2 + [self], player)) == 0:
                    return False
            else:
                self['x'] = newxy[0]
                self['y'] = newxy[1]
                if len(isCheck(pieces + [self], player)) == 0:
                    return False
                else:
                    continue

    return True


def rook_move(self, xy, pieces, player, board, en_passant):
    return rook_or_bishop_move(self, xy, pieces, player, board, [np.array([1,0]), np.array([0,1]), np.array([-1,0]), np.array([0,-1])])


def bishop_move(self, xy, pieces, player, board, en_passant):
    return rook_or_bishop_move(self, xy, pieces, player, board, [np.array([1, 1]), np.array([-1, 1]), np.array([-1, -1]), np.array([1, -1])])


def queen_move(self, xy, pieces, player, board, en_passant):
    if not rook_move(self, xy, pieces, player, board, en_passant):
        return False
    return bishop_move(self, xy, pieces, player, board, en_passant)


def knight_move(self, xy, pieces, player, board, en_passant):
    return king_or_knight_move(self, xy, pieces, player, board, [
        np.array([-2, 1]),np.array([-1, 2]),np.array([1, 2]),np.array([2, 1]),
        np.array([2, -1]),np.array([1, -2]),np.array([-1, -2]),np.array([-2, -1])]
                               )


def pawn_move(self, xy, pieces, player, board, en_passant):
    player_white = player == 0
    enemy = 1 if player_white else 1

    steps = [np.array([0, 1]) if not player_white else np.array([0, -1])]

    # an additional move if a pown does not move
    if player_white and self['y'] == 6:
        steps = steps + [np.array([0, -2])]
    elif not player_white and self['y'] == 1:
        steps = steps + [np.array([0, 2])]

    for dxy in steps:
        newxy = xy + dxy
        if not out_of_range(newxy) and is_empty(board, newxy):
            #can move
            self['x'] = newxy[0]
            self['y'] = newxy[1]
            if len(isCheck(pieces + [self], player)) == 0:
                return False

    #check if we can attack somebody

    steps = [np.array([1, 1]), np.array([-1, 1])] if not player_white else [np.array([1, -1]), np.array([1, -1])]

    for dxy in steps:
        newxy = xy + dxy
        if out_of_range(newxy):
            continue
        if board[newxy[0], newxy[1]]['owner'] == enemy:
            #attack
            pieces2 = pieces.copy()
            for i in range(len(pieces2)):
                if pieces2[i]['x'] == newxy[0] and pieces2[i]['y'] == newxy[1]:
                    pieces2.remove(pieces2[i])
                    break

            self['x'] = newxy[0]
            self['y'] = newxy[1]
            if len(isCheck(pieces2 + [self], player)) == 0:
                return False

        if en_passant is not None and en_passant['prevX'] == newxy[0] and (en_passant['prevY'] + (-1 if not player_white else 1)) == newxy[1]:
            pieces2 = pieces.copy()
            for i in range(len(pieces2)):
                if pieces2[i]['x'] == en_passant['x'] and pieces2[i]['y'] == en_passant['y']:
                    pieces2.remove(pieces2[i])
                    break

            self['x'] = newxy[0]
            self['y'] = newxy[1]
            if len(isCheck(pieces2 + [self], player)) == 0:
                return False

    return True

