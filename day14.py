import hashlib
import collections

version = 'part1'
if version == 'example':
  salt = 'abc'
elif version == 'part1':
  salt = 'yjdafjpo'

hashMax = 0
# threes[18] = '8'
threes = dict()
# fives['e'= [816, 1234, 1801]
fives = dict()

# if lookingFor is set to a char, returns True/False if that char was seen 5x
# if lookingFor not set, returns True/False if a 3x char was found
def buildHash( i, lookingFor = None ):
  global hashMax
  found = False

  if i <= hashMax:
    if lookingFor is None:
      return i in threes
    else:
      return lookingFor in fives

  hashMax = i

  m = hashlib.md5()
  m.update( salt + str(i) )
  h = m.hexdigest()

  threeInARowChar = None
  fiveInARowChar = None

  j = 0
  while (j + 2) < len( h ):
    nextJ = j + 1
    if threeInARowChar is None:
      if h[j] == h[j+1] and h[j] == h[j+2]:
        threeInARowChar = h[j]
        threes[i] = threeInARowChar
        nextJ = j + 3

    if j + 4 < len( h ):
      if h[j] == h[j+1] and h[j] == h[j+2] and h[j] == h[j+3] and h[j] == h[j+4]:
        fiveInARowChar = h[j]
        if fiveInARowChar == lookingFor:
          found = True
        if not fiveInARowChar in fives:
          fives[fiveInARowChar] = []
        fives[fiveInARowChar].append( i )
        nextJ = j + 5

    j = nextJ

  if lookingFor is None:
    return threeInARowChar is not None
  else:
    return found

# -=-=- main -=-=-

i = 0
count = 0
while count < 64:
  #print 'buildHash( %d )' % i
  if buildHash( i ):
    lookForChar = threes[i]
    del threes[i]
    #print "found a three:", i, lookForChar

    stopIdx = i + 1001
    #print 'stopIdx:', stopIdx, 'hashMax:', hashMax
    j = i + 1
    while j <= stopIdx:
      if j <= hashMax:
        #print 'looking in fives'
        j = hashMax
        if lookForChar in fives:
          fiveIdxs = fives[lookForChar]
          #print 'found', lookForChar, 'in fives:', fiveIdxs
          fiveIdxs.sort()
          for fiveIdx in fiveIdxs:
            if fiveIdx > i and fiveIdx <= stopIdx:
              count += 1
              print "  #", count, ', index:', i, ', char:', lookForChar
              j = stopIdx + 1
              continue

      else:
        #print 'buildHash( %d, %s)' % (j, lookForChar)
        if buildHash( j, lookForChar ):
          count += 1
          print "  #", count, ', index:', i, ', char:', lookForChar
          continue

      j += 1
  i += 1


