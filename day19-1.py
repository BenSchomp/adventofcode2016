version = 'part1' # 'example'
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

cur = 0
while True:

  nxt = getNxt( cur )
  #print 'cur:', cur, 'nxt:', nxt, elves

  elves[cur] += elves[nxt]
  elves[nxt] = 0
  if elves[cur] == pIn:
    print "answer: elf #%d" % ( cur + 1 )
    exit()

  cur = getNxt( nxt )

