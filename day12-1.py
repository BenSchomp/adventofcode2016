
file = open('day12-input.txt', 'r')

instr = []
for line in file:
  line = line.rstrip()
  instr.append( line )

i = 0
reg = { 'a': 0, 'b': 0, 'c': 1, 'd': 0 }

def isReg( x ):
  return x >= 'a' and x <= 'd'

while i < len(instr):
  parts = instr[i].split()

  cur = parts[0]
  if cur == 'cpy':
    lhs = parts[1]
    rhs = parts[2]
    if isReg( lhs ):
      reg[rhs] = reg[lhs]
    else:
      reg[rhs] = int(lhs)

  elif cur == 'inc':
    r = parts[1]
    reg[r] += 1

  elif cur == 'dec':
    r = parts[1]
    reg[r] -= 1

  elif cur == 'jnz':
    r = parts[1]
    d = parts[2]
    if isReg( r ):
      val = reg[r]
    else:
      val = int(r)

    if val != 0:
      i += int(d)
      continue

  else:
    print '! illegal instruction:', cur
    exit()

  i += 1

print reg

file.close()
