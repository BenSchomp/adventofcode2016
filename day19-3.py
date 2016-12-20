version = 'xexample'
if version == 'example':
  pIn = 5
else:
  pIn = 3012210

def getNxt( i ):
  n = i
  while True:
    n += 1
    if n >= pIn:
      n = 0
    if elves[n] > 0:
      return n

elves = []
for i in range(pIn):
  elves.append( 1 )
size = len( elves )

cur = 0
while True:

  nxt = cur
  j = int( size / 2 )
  for i in range( j ):
    nxt = getNxt( nxt )

  elves[cur] += elves[nxt]
  elves[nxt] = 0
  size -= 1
  if elves[cur] == pIn:
    print "answer: elf #%d" % ( cur + 1 )
    exit()

  print 'cur:', cur, 'nxt:', nxt, 'size:', size
  cur = getNxt( cur )

