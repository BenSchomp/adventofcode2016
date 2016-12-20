file = open('day20-input.txt', 'r')

blackList = []
for line in file:
  line = line.rstrip()
  parts = line.split( '-' )
  a = int( parts[0] )
  b = int( parts[1] )

  blackList.append( (a,b) )

file.close()
blackList.sort()
print blackList

low = None
high = 4294967295

for i in blackList:
  a = i[0]
  b = i[1]

  if low is None:
    low = b + 1

  else:
    if a <= low and b >= low:
        low = b + 1

print low

