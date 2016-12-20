from collections import deque
import hashlib

version = 'part2'
if version == 'example':
  pIn = 'ihgpwlah'
  pOut = 370
  #pIn = 'kglvqrro'
  #pOut = 492
  #pIn = 'ulqzkmiv'
  #pOut = 830
elif version == 'part2':
  pIn = 'lpvhkcbi'
else:
  exit()

work = deque() # queue to hold all current level of working nodes
work.append( [ pIn, (0,0) ] )
maxSteps = 0

direction = [ 'U', 'D', 'L', 'R' ]
dX = [ 0, 0, -1, 1 ]
dY = [ -1, 1, 0, 0 ]

while len( work ) > 0:
  cur = work.popleft()
  s = cur[0]
  x = cur[1][0]
  y = cur[1][1]

  if x == 3 and y == 3:
    steps = len(s) - len(pIn)
    #print "made it!", steps
    if steps > maxSteps:
      maxSteps = steps

  else:
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

print "maxSteps:", maxSteps
#print "confirm: ", pOut

