file = open('day11-example.txt', 'r')
#file = open('day11-input.txt', 'r')

seen = {}

def move( floors, which, cur, new ):
  print 'move before:', floors, which, cur, new
  for i in which:
    tmp = floors[cur][i]
    floors[cur].remove( tmp )
    floors[new].append( tmp )
    floors[new].sort()
  print 'move after:', floors

  return floors
  

def solve( floors, cur, steps ):
  # seen this position before?
  global seen
  print '+ solve:', floors, ', cur:', cur, ', steps:', steps
  pos = ''
  for floor in floors:
    pos += ''.join( floor ) + '-'
  pos += '-' + str( cur )

  if pos in seen:
    print '! seen this position before'
    return -1
  else:
    seen[pos] = 1

  # puzzle solved?
  if len( floors[0] ) + len( floors[1] ) + len( floors[2] ) == 0:
    print '! solution found'
    return steps
  
  # match up microchips with generators
  tmp = floors[cur]
  for i in tmp:
    if i[1] == 'm':
      for j in tmp:
        if j[0] == i[0] and j[1] == 'g':
          tmp.remove( j[0] + 'm' )
          tmp.remove( j[0] + 'g' )

  # now any chips left are fried if any generators are present
  hasChip = False
  for i in tmp:
    if i[1] == 'm':
      hasChip = True

    if hasChip and i[1] == 'g':
      # fried
      print '! fried', tmp
      return -1

  # try moving each piece up and then down and both dirs in pairs
  print ' -=- move singles -=-'
  for i in range( 0, len( floors[cur] ) ):
    # up
    if cur < 3:
      #solve( move( floors, [i], cur, cur+1 ), cur+1, steps )
      print 'before', floors
      move( floors[:], [i], cur, cur+1 )
      print 'after', floors

    #down
    #solve( move( floors, [i]cur, cur-1 ), cur-1, steps )

  i = 0
  j = 0
  for i in range( 0, len( floors[cur] ) ):
    for j in range( i+1, len( floors[cur] ) ):
      print i, j
      # up
      #solve( move( floors, [i, j], cur, cur+1 ), cur+1, steps )

      #down
      #solve( move( floors, [i, j]cur, cur-1 ), cur-1, steps )

  return floor

# initial setup
print ' -=- Init -=-'
floors =[ [] for i in range(1, 5) ]
f = 0
for line in file:
  line = line.rstrip()

  parts = line.split( ' a ' )
  for part in parts[1:]:
    subParts = part.split()
    print ' %d. ' % f,
    if subParts[1][0:9] == 'generator':
      code = subParts[0][0] + 'g'
      print code
    elif subParts[1][0:9] == 'microchip':
      code = subParts[0][0] + 'm'
      print code

    floors[f].append( code )
    floors[f].sort()
  f += 1

file.close()

print ' -=- begin -=-'
print floors
answer = solve( floors, 0, 0 )
print ' -=- done -=-'
print answer

