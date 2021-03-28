import codewars_test as test
from codewars.knight_check_and_mate import isCheck
from codewars.knight_check_and_mate import isMate

pieces = [
  {'x': 4, 'y': 0, 'owner': 1, 'piece': 'king'},
  {'y': 4, 'x': 1, 'owner': 1, 'prevX': 3, 'prevY': 2, 'piece': 'bishop'},
  {'x': 0, 'y': 7, 'owner': 1, 'piece': 'queen'},
  {'x': 4, 'y': 6, 'owner': 0, 'piece': 'pawn'},
  {'x': 5, 'y': 6, 'owner': 0, 'piece': 'pawn'},
  {'x': 1, 'y': 7, 'owner': 0, 'piece': 'rook'},
  {'x': 3, 'y': 7, 'owner': 0, 'piece': 'bishop'},
  {'x': 4, 'y': 7, 'owner': 0, 'piece': 'king'},
  {'x': 5, 'y': 7, 'owner': 0, 'piece': 'rook'}]

test.assert_equals(isCheck(pieces, 0), [pieces[1]], "bishop threatens king")
test.assert_equals(isMate(pieces, 0), False)

# pieces = [
#   {'y': 3, 'owner': 1, 'piece': 'king', 'x': 5},
#   {'y': 4, 'prevY': 6, 'owner': 0, 'prevX': 4, 'piece': 'pawn', 'x': 4},
#   {'y': 6, 'owner': 0, 'piece': 'pawn', 'x': 5},
#   {'y': 7, 'owner': 0, 'piece': 'king', 'x': 4},
#   {'y': 5, 'owner': 0, 'piece': 'knight', 'x': 2},
#   {'y': 4, 'owner': 1, 'piece': 'pawn', 'x': 3},
#   {'y': 3, 'owner': 1, 'piece': 'knight', 'x': 3},
#   {'y': 3, 'owner': 1, 'piece': 'pawn', 'x': 4},
#   {'y': 2, 'owner': 1, 'piece': 'bishop', 'x': 4},
#   {'y': 2, 'owner': 1, 'piece': 'rook', 'x': 5},
#   {'y': 5, 'owner': 0, 'piece': 'queen', 'x': 6}]
#
# test.assert_equals(isCheck(pieces, 1), [pieces[1]], "pawn threatens king")
# test.assert_equals(isMate(pieces, 1), False)
#
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 3, 'y': 6},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[0]], "King threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "pawn", 'owner': 1, 'x': 5, 'y': 6}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Pawn threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "rook", 'owner': 1, 'x': 4, 'y': 1}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Rook threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "knight", 'owner': 1, 'x': 2, 'y': 6}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Knight threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "bishop", 'owner': 1, 'x': 0, 'y': 3}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Bishop threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "queen", 'owner': 1, 'x': 4, 'y': 1}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Queen threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "queen", 'owner': 1, 'x': 7, 'y': 4}
# ]
# test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Queen threatens king")
# test.assert_equals(isMate(pieces, 0), False)
#
# pieces = [
#   {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
#   {'piece': "pawn", 'owner': 0, 'x': 4, 'y': 6},
#   {'piece': "pawn", 'owner': 0, 'x': 5, 'y': 6},
#   {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
#   {'piece': "bishop", 'owner': 0, 'x': 5, 'y': 7},
#   {'piece': "bishop", 'owner': 1, 'x': 1, 'y': 4},
#   {'piece': "rook", 'owner': 1, 'x': 2, 'y': 7, 'prevX': 2, 'prevY': 5}
# ]
#
# def sortFunc(a,b):
#   if(a['y'] == b['y']): return a['x'] - b['x']
#   return a['y'] - b['y']
#
# test.assert_equals(sorted(isCheck(pieces, 0),key=lambda x: x['y']), [pieces[5], pieces[6]], "Double threat")
