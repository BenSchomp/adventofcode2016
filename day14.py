import hashlib

version = 'part2'
if version[0:7] == 'example':
  salt = 'abc'
elif version[0:4] == 'part':
  salt = 'yjdafjpo'

if version[-1] == '2':
  stretch = 2016
else:
  stretch = 0

# biggest index of pre-calculated hash
hashMax = 0

# threes[ 18 ] = '8'
# threes[ index ] = 'char'
threes = dict()

# fives[ 'char' ] = [ index, index, ... ]
# fives[ 'e' ]= [ 816, 1234, 1801 ]
fives = dict()

# calculate md5 of s
def getHash( s ):
  m = hashlib.md5()
  m.update( s )
  return m.hexdigest()

# if lookingFor is set to a char, returns True/False if that char was seen 5x
# if lookingFor not set, returns True/False if a 3x char was found
# note: this will store off any 3x or 5x that are found in threes and fives
#        for later lookups
def findKeyHash( i, lookingFor = None ):
  global hashMax
  found = False

  if i <= hashMax:
    if lookingFor is None:
      return i in threes
    else:
      return lookingFor in fives

  hashMax = i

  h = getHash( salt + str(i) )
  for y in range( stretch ):
    h = getHash( h )

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
  if findKeyHash( i ):
    lookForChar = threes[i]
    #print "New: '%s' at %d" % ( lookForChar*3, i )
    del threes[i]

    # look for the corresponding 5x from i+1 through i+1000
    j = i + 1
    stopLooking = i + 1000
    while j <= stopLooking:
      if j <= hashMax:
        j = hashMax
        if lookForChar in fives:
          fiveIdxs = fives[lookForChar]
          #print "  Found: '%s' in fives: " % (lookForChar*5), fiveIdxs
          fiveIdxs.sort()
          for fiveIdx in fiveIdxs:
            if fiveIdx > i and fiveIdx <= stopLooking:
              count += 1
              print "--  #%d. '%s' at %d" % ( count, lookForChar*3, i )
              j = stopLooking + 1 # found it, break the outer loop
              continue

      else:
        if findKeyHash( j, lookForChar ):
          count += 1
          print "++  #%d. '%s' at %d" % ( count, lookForChar*3, i )
          continue

      j += 1

  i += 1

print 'Answer:', i-1

