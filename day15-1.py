from copy import deepcopy

# discs[num] = [ size, cur ]
discs = []

example = False
if example:
  # Disc #1 has 5 positions; at time=0, it is at position 4.
  # Disc #2 has 2 positions; at time=0, it is at position 1.
  discs.append( [ 5, 4 ] )
  discs.append( [ 2, 1 ] )

else:
  # Disc #1 has 7 positions; at time=0, it is at position 0.
  # Disc #2 has 13 positions; at time=0, it is at position 0.
  # Disc #3 has 3 positions; at time=0, it is at position 2.
  # Disc #4 has 5 positions; at time=0, it is at position 2.
  # Disc #5 has 17 positions; at time=0, it is at position 0.
  # Disc #6 has 19 positions; at time=0, it is at position 7.
  discs.append( [ 7, 0 ] )
  discs.append( [ 13, 0 ] )
  discs.append( [ 3, 2 ] )
  discs.append( [ 5, 2 ] )
  discs.append( [ 17, 0 ] )
  discs.append( [ 19, 7 ] )

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

