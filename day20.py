version = "part2"
if version == "example":
  file = open('day20-example.txt', 'r')
  maxIp = 9
elif version[0:-1] == "part":
  file = open('day20-input.txt', 'r')
  maxIp = 4294967295

blacklist = []
foo = {}
for line in file:
  line = line.rstrip()
  parts = line.split( '-' )
  a = int( parts[0] )
  b = int( parts[1] )
  
  if b <= a:
    print a, b
    exit()

  blacklist.append( (a,b) )

  if a in foo:
    print 'exists:', a
    exit()
  foo[a] = 0
  if b in foo:
    print 'exists:', b
    exit()
  foo[b] = 1

file.close()

i = None
j = None
count = 0
blacklist.sort()
for k in blacklist:
  if i == None:
    i = k[0]
    count = k[0]
    j = k[1]
    continue

  if k[0] - j > 1:
    #print " *gap"
    if version == "part1":
      print "First:", j+1
      exit()
    count += k[0] - j - 1 # inclusive
    i = k[0]
    j = k[1]

  if k[1] > j:
    j = k[1]

  #print k, "i:", i, ", j:", j, ", count:", count

count += maxIp - j
print "Count:", count

