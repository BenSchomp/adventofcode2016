n = 3012210
part = 2

elves = [ 1 ] * n

def getNext( x ):
  while True:
    x += 1
    if x == n:
      x = 0
    if elves[x] == 1:
      break
  return x

if part == 1:
  cur = 1 # first steal is from the elf on the left
else:
  cur = int( n / 2 ) # first steal is from across the circle

count = 0
skip = ( n % 2 != 0 )
while True:
  # steal
  elves[cur] = 0
  cur = getNext( cur )

  count += 1
  if count >= n-1: # only need n-1 steals
    break

  if part == 2: # skip every-other (xOxOxO...)
    skip = not skip
    if skip:
      continue
  cur = getNext( cur )

print 'answer: elf #%d' % (elves.index( 1 ) + 1)
