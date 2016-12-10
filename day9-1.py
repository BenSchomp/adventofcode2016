#file = open('day9-example.txt', 'r')
file = open('day9-input.txt', 'r')

for line in file:
  line = line.rstrip()
  print line
  out = ''
  i = 0
  while i < len( line ):
    if line[i] == '(':
      j = i+1
      while line[j] != ')':
        j += 1

      marker = line[i+1:j]
      parts = marker.split('x')
      chars = int(parts[0])
      repeat = int(parts[1])

      text = line[j+1:j+1+chars]
      for i in range( repeat ):
        out += text
      
      i = j + chars

    else:
      out += line[i]

    i += 1

  print out, len(out)


file.close()
