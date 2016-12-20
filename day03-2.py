file = open('day03-input.txt', 'r')

def isValid( sides ):
  sides.sort()
  return sides[0] + sides[1] > sides[2]

valid = 0

while True:
  a = file.readline()
  b = file.readline()
  c = file.readline()

  if a == '' or b == '' or c == '':
    break

  aRow = map( int, a.split() )
  bRow = map( int, b.split() )
  cRow = map( int, c.split() )

  for i in range( 3 ):
    if isValid( [ aRow[i], bRow[i], cRow[i] ] ):
      valid += 1

print "valid: ", valid
file.close()
