version = 'example'
if version == 'part2':
  pIn = 3012210
else:
  pIn = 5

# each elf has [orig_idx, #_presents]
elves = []
for i in range(pIn):
  elves.append( [i,1] )
size = pIn

def getNthNextPos( i, n ):
  result = i

  while n > 0:
    result += 1
    if result > size:
      result = 0
    n -= 1

  return result

i = iter( elves )
while True:
  cur = i.next()
  curIdx = cur[0]

  j = int( size / 2 )
  nxtIdx = ( cur[0] + j ) % size

  print 'cur:', curIdx, 'nxt:', nxtIdx, elves

  elves[curIdx][1] += elves[nxtIdx][1]
  if elves[curIdx][1] == pIn:
    print "answer: elf #%d" % ( elves[curIdx][0] + 1 )
    exit()

  elves.pop(nxtIdx)
  size -= 1
  #if not size % 10000:
    #print size


