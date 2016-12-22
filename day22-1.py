file = open('day22-input.txt', 'r')

nodes = dict()
for line in file:
  line = line.rstrip()
  parts = line.split()
  #print parts

  location = parts[0].split( '-' )
  x = ( location[1][1:] )
  y = ( location[2][1:] )

  #print x, y

  used = int( parts[2][:-1] )
  avail = int( parts[3][:-1] )

  #print used, avail

  loc = x + ',' + y
  nodes[loc] = ( used, avail )

file.close()

count = 0
for key1, a in nodes.iteritems():
  for key2, b in nodes.iteritems():
    #print a, b
    if a[0] == 0:
      continue

    if key1 == key2:
      continue

    if a[0] > b[1]:
      continue

    count += 1

print count
