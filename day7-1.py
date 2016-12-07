#file = open('day7-example.txt', 'r')
file = open('day7-input.txt', 'r')

def isABBA( word ):
  i = 0
  j = i + 3
  while j < len( word ):
    if word[i] != word[i+1] and word[i] == word[j] and word[i+1] == word[j-1]:
      return True

    i += 1
    j += 1

  return False

count = 0
for line in file:
  line = line.rstrip()
  outsides = []
  insides = []
  parts = line.split( '[' )
  outsides.append( parts[0] )

  for part in parts[1:]:
    subparts = part.split( ']' )
    insides.append( subparts[0] )
    outsides.append( subparts[1] )

  foundInside = False
  for inside in insides:
    if isABBA( inside ):
      foundInside = True
      break

  if not foundInside:
    for outside in outsides:
      if isABBA( outside ):
        count += 1
        break

print "count:", count
file.close()
