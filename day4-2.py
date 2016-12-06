import operator

def shiftCipher( word, shifts ):
  shift = shifts % 26
  low = ord( 'a' )
  high = ord( 'z' )

  result = ''
  for i in range( 0, len(word) ):
    cur = ord( word[i] )
    if cur < low or cur > high:
      result += ' '
    else:
      cur += shift
      if cur > high:
        cur -= 26
      result += chr( cur )

  return result

file = open('day4-input.txt', 'r')

answer = 0
for line in file:
  parts = line.split( '[' )
  checksum = parts[1][0:5]
  
  parts = parts[0].rsplit( '-', 1 )
  name = parts[0]
  sectorid = int(parts[1])

  counts = {}

  for i in range( 0, len(name) ):
    if name[i] != '-':
      if not name[i] in counts:
        counts[name[i]] = 1
      else:
        counts[name[i]] += 1

  # sort the dictionary by value
  sortedcounts = sorted( counts.items(), key=operator.itemgetter(1) )
  sortedcounts.reverse()

  numcounts = len(sortedcounts)
  testchecksum = ''

  i = 0
  while i < numcounts:
    cur = sortedcounts[i][1]

    subgroup = [ sortedcounts[i][0] ]

    j = i+1
    while j < numcounts:
      if sortedcounts[j][1] == cur:
        i = j
        subgroup.append( sortedcounts[j][0] )
      j += 1

    sortedsubgroup = sorted( subgroup )
    testchecksum += ''.join(sortedsubgroup)
    i += 1

  testchecksum = testchecksum[:5]
  if checksum == testchecksum:
    answer += sectorid
    #print answer, name, sectorid, checksum, testchecksum
    print sectorid, shiftCipher( name, sectorid )

print answer
file.close()

