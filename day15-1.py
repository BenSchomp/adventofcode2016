from copy import deepcopy

# discs[num] = [ size, cur ]
discs = []

version = 'day1' # example, day1, day2
if version == 'example':
  discs.append( [ 5, 4 ] )
  discs.append( [ 2, 1 ] )

elif version[0:3] == 'day':
  discs.append( [ 7, 0 ] )
  discs.append( [ 13, 0 ] )
  discs.append( [ 3, 2 ] )
  discs.append( [ 5, 2 ] )
  discs.append( [ 17, 0 ] )
  discs.append( [ 19, 7 ] )

if version[3] == '2':
  discs.append( [ 11, 0 ] )


def advance( d, tDelta ):
  canDrop = True
  tDelta += 1
  for cur in d:
    cur[1] += tDelta
    cur[1] = cur[1] % cur[0]
    #print tDelta, cur
    if cur[1] != 0:
      #print " * can't drop"
      return False
    tDelta += 1

  return canDrop

t = -1
done = False
print "Init:", discs
while not done:
  t += 1
  done = advance( deepcopy( discs ), t )

print "done, t =", t

