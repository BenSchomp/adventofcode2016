from collections import deque
import hashlib

work = deque() # queue to hold all current level of working nodes

pIn = 'hijkl'
pOut = 'no solution'
pIn = 'ihgpwlah'
pOut = 'DDRRRD'
pIn = 'kglvqrro'
pOut = 'DDUDRLRRUDRD'
pIn = 'ulqzkmiv'
pOut = 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

work.append( [ pIn, (0,0) ] )

direction = [ 'U', 'D', 'L', 'R' ]
dX = [ 0, 0, -1, 1 ]
dY = [ -1, 1, 0, 0 ]

while len( work ) > 0:
  cur = work.popleft()
  s = cur[0]
  x = cur[1][0]
  y = cur[1][1]
  #print s, x, y

  if x == 3 and y == 3:
    print "made it!"
    print "answer: ", s[len(pIn):]
    print "confirm:", pOut
    exit()

  m = hashlib.md5()
  m.update( s )
  h = m.hexdigest()

  # 0:up, 1:down, 2:left, 3:right
  # b,c,d,e,f means open
  for i in range(4):
    if h[i] >= 'b' and h[i] <= 'f':
      curX = x + dX[i]
      curY = y + dY[i]
      if curX < 0 or curX > 3 or curY < 0 or curY > 3:
        continue

      work.append( [ s + direction[i], ( curX, curY ) ] )

print 'no solution'

