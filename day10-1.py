#file = open('day10-example.txt', 'r')
file = open('day10-input.txt', 'r')

answer = ''
bots = {}

queue = []
for line in file:
  queue.append( line.rstrip() )

i = 0
while len( queue ) > 0:
  parts = queue[i].split()

  if parts[0] == 'value':
    print queue[i]
    botId = parts[4] + parts[5]
    if not botId in bots:
      bots[botId] = []
    bots[botId].append( int(parts[1]) )
    bots[botId].sort()

  elif parts[0] == 'bot':
    fromId = parts[0] + parts[1]
    if fromId in bots and len( bots[fromId] ) == 2:
      print queue[i]
      lowToId = parts[5] + parts[6]
      if not lowToId in bots:
        bots[lowToId] = []

      highToId = parts[10] + parts[11]
      if not highToId in bots:
        bots[highToId] = []
      
      if bots[fromId] == [17,61]:
        answer = fromId
      
      lowChip = bots[fromId][0]
      highChip = bots[fromId][1]
      bots[fromId] = []

      bots[lowToId].append( lowChip )
      bots[highToId].append( highChip )

      bots[lowToId].sort()
      bots[highToId].sort()
    else:
      i += 1
      continue

  del queue[i]
  i = 0

  #print bots

print answer
print bots['output0'], bots['output1'], bots['output2']
print int(bots['output0'][0]) * int(bots['output1'][0]) * int(bots['output2'][0])

file.close()
