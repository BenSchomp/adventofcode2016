#file = open('day9-example.txt', 'r')
file = open('day9-input.txt', 'r')

def decompress( word ):
  count = 0
  i = 0
  while i < len(word):
    if word[i] == '(':
      j = i + 1
      while j < len(word):
        if word[j] == ')':
          key = word[i+1:j]
          break
        j += 1
      parts = key.split('x')
      chars = int(parts[0])
      repeat = int(parts[1])
      nextWord = word[j+1:j+1+chars]
      count += repeat * decompress( nextWord )
      i = j+chars
    else:
      count += 1

    i += 1

  #print "  decompress:", word, count
  return count

for line in file:
  line = line.rstrip()
  print line

  answer = decompress( line )
  print "answer:", answer

file.close()

