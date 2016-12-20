import hashlib
import collections

salt = 'abc'
# hashes[10] = [ <first_3InARow>, [ <first_5InARow>, <second_5InARow>, ... ] ]
# hashes[15] = [ 'a', [ ] ]
# hashes[17] = [ '7', [ '7', 'x' ] ]
threes = []
hashes = dict()

def buildHash( i ):
  global hashes
  if i not in hashes.keys():
    m = hashlib.md5()
    m.update( salt + str(i) )
    h = m.hexdigest()

    threeInARowChar = None
    fiveInARowChars = []
    j = 0
    while (j + 2) < len( h ):
      nextJ = j + 1
      if threeInARowChar is None:
        if h[j] == h[j+1] and h[j] == h[j+2]:
          threeInARowChar = h[j]
          nextJ = j + 3
          # look for a five from i+1 through i+1000
          iMax = i + 1001

      if j + 4 < len( h ):
        if h[j] == h[j+1] and h[j] == h[j+2] and h[j] == h[j+3] and h[j] == h[j+4]:
          fiveInARowChars.append( h[j] )
          nextJ = j + 5

      j = nextJ

    hashes[i] = [ i, s, h, threeInARowChar, fiveInARowChars ]

i = 0
count = 0

while count < 64:
  if i not in hashes.keys():
    m = hashlib.md5()
    m.update( salt + str(i) )
    h = m.hexdigest()

    threeInARowChar = None
    fiveInARowChars = []
    j = 0
    while (j + 2) < len( h ):
      nextJ = j + 1
      if threeInARowChar is None:
        if h[j] == h[j+1] and h[j] == h[j+2]:
          threeInARowChar = h[j]
          nextJ = j + 3
          # look for a five from i+1 through i+1000
          iMax = i + 1001

      if j + 4 < len( h ):
        if h[j] == h[j+1] and h[j] == h[j+2] and h[j] == h[j+3] and h[j] == h[j+4]:
          fiveInARowChars.append( h[j] )
          nextJ = j + 5

      j = nextJ

    hashes[i] = [ i, s, h, threeInARowChar, fiveInARowChars ]

  if len( fiveInARowChars ):
    print threes
    for fiveChar in fiveInARowChars:
      for three in threes:
        threeIndx = three[0]
        threeChar = three[1]
        #print i, three, five
        if threeIndx + 1001 < i:
          # 1000 seen for this three, no corresponding five: remove it
          threes.remove( three )

        if threeChar == fiveChar:
          print "found one: ", i, three
          threes.remove( three )
          count += 1

  if threeInARowChar is not None:
    # [ (18, '8'), (39, 'e') ]
    threes.append( (i, threeInARowChar) )

  i += 1

#print threes
#print fives

#for k,v in hashes.items():
  #print v
