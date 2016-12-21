from copy import deepcopy

version = "part1"
if version == "example":
  file = open('day21-example.txt', 'r')
  pIn = 'abcde'
elif version[0:-1] == "part":
  file = open('day21-input.txt', 'r')
  pIn = 'abcdefgh'


def bail():
  print ' ! bad command'
  exit()

def display( x ):
  print ' ', ''.join( x )

def swap( s, x, y ):
  tmp = s[x]
  s[x] = s[y]
  s[y] = tmp

s = list( pIn )
l = len( s )
print 'init'
display( s )
for line in file:
  line = line.rstrip()
  parts = line.split()
  cmd = parts[0]
  what = parts[1]

  if cmd == 'swap':
    print 'swap:',
    if what == 'position':
      x = int( parts[2] )
      y = int( parts[5] )
      print 'position', x, y
      swap( s, x, y )

    elif what == 'letter':
      x = parts[2]
      y = parts[5]
      print 'letter', x, y
      for i in range( l ):
        if s[i] == x:
          s[i] = y
        elif s[i] == y:
          s[i] = x

    else:
      bail()

  elif cmd == 'rotate':
    print 'rotate:',
    if what == 'left':
      steps = int(parts[2]) * -1
      print 'left',
    elif what == 'right':
      steps = int(parts[2])
      print 'right',
    elif what == 'based':
      idx = s.index( parts[6] )
      steps = 1 + idx
      if idx >= 4:
        steps += 1
      print 'based on position', idx,
    else:
      bail()

    print '(%d)' % steps
    steps *= -1
    tmp = deepcopy(s)
    for i in range( l ):
      s[i] = tmp[(i + steps) % l]

  elif cmd == 'reverse':
    if what == 'positions':
      x = int(parts[2])
      y = int(parts[4])
      print 'reverse: positions', x, y
      for i in range( (y - x + 1) / 2 ):
        swap( s, i+x, y-i )

    else:
      bail()

  elif cmd == 'move':
    if what == 'position':
      x = int(parts[2])
      y = int(parts[5])
      print 'move: position', x, y
      tmp = s.pop( x )
      s.insert( y, tmp )
    else:
      bail()

  else:
    bail()

  display( s )

file.close()
