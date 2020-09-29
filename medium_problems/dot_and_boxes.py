from itertools import chain

def dots_and_boxes(moves):
    nodes = 1+max(chain.from_iterable(moves))
    player, Y = 0, int(nodes**.5)
    pts, grid = [0,0], [4]*nodes
    
    for a,b in moves:
        swap = 1
        if a>b: a,b = b,a
        for i in (a, a-Y if b-a==1 else a-1):
            if i<0: continue
            grid[i] -= 1
            if not grid[i]:
                pts[player] += 1 ; swap = 0
        player ^= swap
        
    return tuple(pts)


from math import floor
def dots_and_boxes(moves):
    n = max(sum(moves, ()))
    n = floor(n ** .5) + 1
    pairs = {((i,i+n),(i,i+1),(i+1,i+1+n),(i+n,i+1+n)) for j in range(0,n*n-n,3) for i in range(j,j+(n-1))}
    turn,prev,total,d = 0,0,set(),{0: 0, 1: 0}
    for i in moves:
        total.add(i)
        r = sum(all(j in total or j[::-1] in total for j in k) for k in pairs)
        if r > prev:
            d[turn] += r - prev
            prev = r ; continue
        turn ^= 1
    return d[0],d[1]

def vertices2edges(*vertices):
    return frozenset(map(frozenset, zip(vertices, vertices[1:] + vertices)))

def bording_boxes(a, b):
    return {vertices2edges(a, a + (a-b) * side, b + (a-b) * side, b) for side in (1j, -1j)}

def coordinates(edge, width):
    return frozenset(complex(*divmod(dot, width)) for dot in edge)

def dots_and_boxes(moves):
    grid, size = set(), int((len(moves) // 2) ** .5) + 1
    player, scores = False, [0, 0]
    for move in moves:
        move2D = coordinates(move, size)
        grid.add(move2D)
        score = sum(box <= grid for box in bording_boxes(*move2D))
        scores[player] += score
        if not score: player = not player
    return tuple(scores)


import math
from collections import defaultdict

get_coordinates = lambda x,n: (x // n, x%n)
get_point_squares = lambda x, n: {i for i in 
    [(x[0]-1, x[1]-1), (x[0]-1, x[1]), (x[0],x[1]-1), (x[0],x[1])] if i[0]>=0 and i[1] >= 0 and i[0] <= (n-2) and i[1] <= (n-2)}
get_touching_square = lambda coor, n: get_point_squares(get_coordinates(coor[0], n), n) & get_point_squares(get_coordinates(coor[1], n), n)

def dots_and_boxes(ar):
  n = math.ceil(math.sqrt(len(ar) /2))
  grid, wins, player_turn_adjust = defaultdict(int), [0,0], 0
  for turn,line in enumerate(ar):
      turn_win = False
      squares = get_touching_square(line, n)
      for square in squares:
          grid[square] += 1
          if grid[square] == 4:
              wins[(turn+player_turn_adjust) %2] += 1
              turn_win = True
      if turn_win:
          player_turn_adjust = 1 - player_turn_adjust
          

  return (wins[0], wins[1])