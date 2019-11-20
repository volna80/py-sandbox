import codewars_test as test
from codewars.Solution_check_and_mate import isCheck

pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "pawn", 'owner': 1, 'x': 5, 'y': 6}
]
test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Pawn threatens king")

pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "rook", 'owner': 1, 'x': 4, 'y': 1}
]
test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Rook threatens king")


pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "knight", 'owner': 1, 'x': 2, 'y': 6}
]
test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Knight threatens king")

pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "bishop", 'owner': 1, 'x': 0, 'y': 3}
]
test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Bishop threatens king")

pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "queen", 'owner': 1, 'x': 4, 'y': 1}
]
test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Queen threatens king")

pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "queen", 'owner': 1, 'x': 7, 'y': 4}
]
test.assert_equals(isCheck(pieces, 0), [pieces[2]], "Queen threatens king")

pieces = [
  {'piece': "king", 'owner': 1, 'x': 4, 'y': 0},
  {'piece': "pawn", 'owner': 0, 'x': 4, 'y': 6},
  {'piece': "pawn", 'owner': 0, 'x': 5, 'y': 6},
  {'piece': "king", 'owner': 0, 'x': 4, 'y': 7},
  {'piece': "bishop", 'owner': 0, 'x': 5, 'y': 7},
  {'piece': "bishop", 'owner': 1, 'x': 1, 'y': 4},
  {'piece': "rook", 'owner': 1, 'x': 2, 'y': 7, 'prevX': 2, 'prevY': 5}
]

def sortFunc(a,b):
  if(a['y'] == b['y']): return a['x'] - b['x']
  return a['y'] - b['y']

test.assert_equals(sorted(isCheck(pieces, 0),key=lambda x: x['y']), [pieces[5], pieces[6]], "Double threat")
