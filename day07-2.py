#file = open('day07-example.txt', 'r')
file = open('day07-input.txt', 'r')

def getABA( word ):
  i = 0
  j = i + 2
  aba = []
  while j < len( word ):
    if word[i] != word[i+1] and word[i] == word[j] and word[i+1] == word[j-1]:
      aba.append( word[i:j+1] )

    i += 1
    j += 1

  return aba

def isMatch( aba, bab ):
  for a in aba:
    for b in bab:
      if a[0] == b[1] and a[1] == b[0]:
        return True
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

  hypernet = []
  for inside in insides:
    hypernet.extend( getABA( inside ) )

  supernet = []
  for outside in outsides:
    supernet.extend( getABA( outside ) )

  if isMatch( hypernet, supernet ):
    count += 1
    print count, hypernet, " MATCHES ", supernet

print "count:", count
file.close()
