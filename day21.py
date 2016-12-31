from copy import deepcopy
import sys

version = "part2"
if version == "example":
  file = open('day21-example.txt', 'r')
  pIn = 'abcde'
  unscramble = False
elif version == "part1":
  file = open('day21-input.txt', 'r')
  pIn = 'abcdefgh'
  unscramble = False
elif version == "part2":
  file = open('day21-input.txt', 'r')
  pIn = 'fbgdceah'
  unscramble = True

lines = []
for line in file:
  lines.append( line )

file.close()

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

if unscramble:
  lines.reverse()

for line in lines:
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
      print 'based on position', idx,

      # Deterministic when password is length 8 ...
      # x....... >>> .x......  (0 to 1) >> unscrabmle >> (1 to 0) or 1:-1 steps
      # .x...... >>> ...x....  (1 to 3)                  (3 to 1) or 3:-2 steps
      # ..x..... >>> .....x..  (2 to 5)                  (5 to 2) or 5:-3 steps
      # ...x.... >>> .......x  (3 to 7)                  (7 to 3) or 7:-4 steps
      # ....x... >>> ..x.....  (4 to 2)                  (2 to 4) or 2:+2 steps
      # .....x.. >>> ....x...  (5 to 4)                  (4 to 5) or 4:+1 steps
      # ......x. >>> ......x.  (6 to 6)                  (6 to 6) or 6:0 steps
      # .......x >>> x.......  (7 to 0)                  (0 to 7) or 0:-1 steps

      if unscramble:
        steps = -[ -1, -1, +2, -2, +1, -3, 0, -4 ][idx]
      else:
        steps = 1 + idx
        if idx >= 4:
          steps += 1
    else:
      bail()

    if not unscramble:
      steps *= -1
    print '(%d)' % steps

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
      if unscramble:
        tmp = x
        x = y
        y = tmp
      print 'move: position', x, y
      tmp = s.pop( x )
      s.insert( y, tmp )
    else:
      bail()

  else:
    bail()

  display( s )

