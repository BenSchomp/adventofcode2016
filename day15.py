from copy import deepcopy

# discs[num] = [ size, cur ]
discs = []

version = 'part1' # example, part1, part2
if version == 'example':
  discs.append( [ 5, 4 ] )
  discs.append( [ 2, 1 ] )

elif version[0:-1] == 'part':
  discs.append( [ 7, 0 ] )
  discs.append( [ 13, 0 ] )
  discs.append( [ 3, 2 ] )
  discs.append( [ 5, 2 ] )
  discs.append( [ 17, 0 ] )
  discs.append( [ 19, 7 ] )

if version[-1] == '2':
  discs.append( [ 11, 0 ] )

print version, version[0:-1], version[-1]


def advance( d, tDelta ):
  canDrop = True
  tDelta += 1
  for cur in d:
    cur[1] += tDelta
    cur[1] = cur[1] % cur[0]
    if cur[1] != 0:
      return False
    tDelta += 1

  return canDrop

t = -1
done = False
print "Init:", discs
while not done:
  t += 1
  if t % 100000 == 0:
    print "  t =", t
  done = advance( deepcopy( discs ), t )

print "* t =", t

