from copy import deepcopy
from collections import deque

# -=-=- helpers -=-=-

def getKey( state ):
  result = ''
  for k in sorted( state ):
    if k < 0:
      continue
    result += '|%d:%d,%d' % (k, state[k][0], state[k][1])

  return result

def display( state ):
  global rows
  row = 0
  for i in rows:
    r = ''
    col = 0
    for j in i:
      if (col, row) in state.values():
        for k, v in state.iteritems():
          if v == (col, row):
            r += str(k)
      else:
        r += j
      col += 1
    row += 1
    print r
  print '  Steps:', state[-1]
  print

# -=-=- init setup -=-=-

#file = open('day24-example.txt', 'r')
file = open('day24-input.txt', 'r')

# part 1: hit all locations
# part 2: return home
goHome = False

# locs[0]:  current position
# locs[-1]: current number of steps
# locs[-2]: starting/home location
locs = dict()
locs[-1] = 0

rows = []
curRow = 0
for line in file:
  line = line.rstrip()

  width = len( line )

  row = []
  for col in range( width ):
    cur = line[col]

    if cur == '#':
      row.append( '#' )
    else:
      row.append( '.' )

      if cur != '.':
        locs[int(cur)] = (col, curRow)
      if cur == '0':
        # note: setting neg values to avoid false match in display()
        locs[-2] = (-col, -curRow)
  
  rows.append( row )
  curRow += 1

work = deque()
seen = dict()

work.append( locs )
seen[ getKey(locs) ] = 1
display( locs )

file.close()

# -=-=- go for it! -=-=-

level = 0
while len( work ) > 0:
  parent = work.popleft()

  curX = parent[0][0]
  curY = parent[0][1]

  # try moving
  for dX in [-1, 0, 1]:
    for dY in [-1, 0, 1]:
      if abs(dX) == abs(dY):
        # no diag or staying put
        continue

      newX = curX + dX
      newY = curY + dY
      if rows[newY][newX] == '.':
        cur = deepcopy( parent )
        cur[0] = (newX, newY)
        cur[-1] += 1
        
        for i, value in cur.iteritems():
          if i < 1:
            continue

          if (newX, newY) == value:
            del cur[i]

            if len( cur ) < 4:
              if -2 in cur:
                print "Cleared locations in %d Steps ... now return to start." % cur[-1]
                goHome = True
                # since the locations are cleared out:
                #  a. set an item to the non-negative location
                #  b. reset the seen and work queues
                #  c. just walk on home
                cur[1] = ( -cur[-2][0], -cur[-2][1] )
                del cur[-2]
                cur[-3] = 'dummy' # just to keep the count even
              else:
                print "Done."
                display( cur )
                exit()

            break

        key = getKey( cur )
        if key not in seen:
          work.append( cur )
          seen[key] = 1

  level += 1

print "shouldn't get here"

