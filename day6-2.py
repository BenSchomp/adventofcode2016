import operator

file = open('day6-input.txt', 'r')

numcols = 0
cols = []
for line in file:
  numcols = len(line)
  for i in range(0, numcols-1):
    if len(cols) < i+1:
      d = {}
      d[line[i]] = 1
      cols.append( d )
    elif not line[i] in cols[i]:
      cols[i][line[i]] = 1
    else:
      cols[i][line[i]] += 1

file.close()

# sort the dictionaries by value
answer = ''
for i in range(0, numcols-1):
  sortedcols = sorted( cols[i].items(), key=operator.itemgetter(1) )
  answer += sortedcols[0][0]

print answer
