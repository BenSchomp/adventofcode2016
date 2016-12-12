from copy import deepcopy

file = open('day11-example.txt', 'r')
#file = open('day11-input.txt', 'r')

# floors = { 0: cur, 1: [ ], 2: [ ], 3: [ ], 4: [ ] }

def getCur( floors ):
  return floors[0][0]

def setCur( floors, cur ):
  floors[0][0] = cur

def display( floors, text = '' ):
  print text
  for i in range( 4, 0, -1 ):
    print 'f%d:' % i,
    print '*' if getCur( floors ) == i else ' ',
    print ' '.join( floors[i] )

def move( floors, items, to ):
  items.sort( reverse=True )
  cur = getCur( floors )
  for i in items:
    tmp = floors[cur][i]
    floors[cur].remove( tmp )
    floors[to].append( tmp )
    floors[to].sort()
  setCur( floors, to )

seen = {}
def solve( floors, steps ):
  #display( floors, '+ solve:' )

  # seen this position before?
  global seen
  cur = getCur( floors )
  numItems = len( floors[cur] )

  pos = ''
  for floor in floors[1:]:
    pos += ''.join( floor ) + '-'
  pos += str( cur )

  if pos in seen:
    #print '! seen this position before'
    return -1
  else:
    seen[pos] = 1

  # puzzle solved?
  if len( floors[1] ) + len( floors[2] ) + len( floors[3] ) == 0:
    print '*** solution found (%d) ***' % steps
    print floors
    return steps
  
  # match up microchips with generators
  tmp = deepcopy( floors[cur] )
  chips = []
  generators = []
  for i in tmp:
    if i[1] == 'm':
      chips.append( i )
    elif i[1] == 'g':
      generators.append( i )
    else:
      exit()

  matches = 0
  for i in chips:
    for j in generators:
      if i[0] == j[0]:
        matches += 1
        break

  if len( generators ) > matches and len( chips ) > matches:
    #print '! fried', tmp
    return -1
  
  # try moving each piece up and then down and both dirs in pairs
  orig = deepcopy( floors )
  for i in range( 0, numItems ):
    # up
    if cur < 4:
      floors = deepcopy( orig )
      move( floors, [i], cur+1 )
      result = solve( floors, steps+1 )
      if result > 0:
        return result

    #down
    if cur > 1:
      floors = deepcopy( orig )
      move( floors, [i], cur-1 )
      result = solve( floors, steps+1 )
      if result > 0:
        return result

  for i in range( 0, numItems ):
    for j in range( i+1, numItems ):
      # up
      if cur < 4:
        floors = deepcopy( orig )
        move( floors, [i, j], cur+1 )
        result = solve( floors, steps+1 )
        if result > 0:
          return result

      #down
      if cur > 1:
        floors = deepcopy( orig )
        move( floors, [i, j], cur-1 )
        result = solve( floors, steps+1 )
        if result > 0:
          return result

  return -1

# initial setup
floors =[ [] for i in range(0, 5) ]
floors[0].append( 1 )
i = 1
for line in file:
  line = line.rstrip()

  parts = line.split( ' a ' )
  for part in parts[1:]:
    subParts = part.split()
    if subParts[1][0:9] == 'generator':
      code = subParts[0][0] + 'g'
    elif subParts[1][0:9] == 'microchip':
      code = subParts[0][0] + 'm'

    floors[i].append( code )
    floors[i].sort()
  i += 1

file.close()
#display( floors, '+ Init' )

print ' -=- begin -=-'
display( floors )
answer = solve( floors, 0 )
print ' -=- done -=-'
print answer

