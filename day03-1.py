file = open('day03-input.txt', 'r')

valid = 0
for line in file:
  sides = map( int, line.split() )
  sides.sort()
  if sides[0] + sides[1] > sides[2]:
    valid += 1


print "valid: ", valid
file.close()
