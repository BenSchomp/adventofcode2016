from collections import deque

end = (31, 39)
puzzleInput = 1352

version = 'part1'

def isOpen( x, y ):
  result = x*x + 3*x + 2*x*y + y + y*y
  result += puzzleInput

  binary = "{0:b}".format( result )
  ones = binary.count( '1' )

  return ( ones % 2 == 0 )

def key( x, y ):
  key = "%d,%d" % (x,y)
  return key

def display( h, w ):
  print '  0123456789'
  for i in range (h):
    row = '%d ' % i
    for j in range (w):
      if isOpen( j, i ):
        row += '.'
      else:
        row += '#'

    print row

#display( 7, 10)

seen = dict()
work = deque() # queue to hold all current level of working nodes

seen[ key(1,1) ] = 1
work.append( ( (1, 1), 0 ) )

while len( work ) > 0:
  cur = work.popleft()
  ( loc, depth ) = cur[0], cur[1]

  if version == 'part2' and depth > 49:
    print len( seen )
    exit()

  if loc == end:
    print "min steps:", depth
    exit()

  for (xd,yd) in ( (-1,0), (1,0), (0,-1), (0,1) ):
    x = loc[0] + xd
    y = loc[1] + yd

    if x < 0 or y < 0:
      continue

    if key(x,y) in seen:
      continue

    if isOpen( x, y ):
      seen[ key(x,y) ] = 1
      work.append( ( (x,y), depth+1 ) )

