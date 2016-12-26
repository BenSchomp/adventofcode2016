i = 0
reg = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }

version = 'part1'
if version == 'example':
  file = open('day23-example.txt', 'r')
elif version == 'part1':
  file = open('day23-input.txt', 'r')
  reg['a'] = 7

instr = []
for line in file:
  line = line.rstrip()
  instr.append( line )

file.close()

def toggle( x ):
  cmd = instr[x]
  parts = cmd.split()
  cur = parts[0]

  if cur == 'inc':
    cmd = cmd.replace( 'inc', 'dec', 1 )
  elif cur == 'dec':
    cmd = cmd.replace( 'dec', 'inc', 1 )
  elif cur == 'tgl':
    cmd = cmd.replace( 'tgl', 'inc', 1 )
  elif cur == 'jnz':
    cmd = cmd.replace( 'jnz', 'cpy', 1 )
  elif cur == 'cpy':
    cmd = cmd.replace( 'cpy', 'jnz', 1 )

  instr[x] = cmd

def isReg( x ):
  return x >= 'a' and x <= 'd'

while i >= 0 and i < len(instr):
  #print i, instr, reg

  parts = instr[i].split()

  cur = parts[0]
  if cur == 'cpy': # two args
    lhs = parts[1]
    rhs = parts[2]
    if isReg( rhs ):
      if isReg( lhs ):
        reg[rhs] = reg[lhs]
      else:
        reg[rhs] = int(lhs)
    else:
      # bad cpy, ignore
      pass

  elif cur == 'inc': # one arg
    r = parts[1]
    reg[r] += 1

  elif cur == 'dec': # one arg
    r = parts[1]
    reg[r] -= 1

  elif cur == 'jnz': # two args
    lhs = parts[1]
    rhs = parts[2]
    if isReg( lhs ):
      val = reg[lhs]
    else:
      val = int(lhs)

    if isReg( rhs ):
      jump = reg[rhs]
    else:
      jump = int(rhs)

    if val != 0:
      i += jump
      continue

  elif cur == 'tgl': # one arg
    r = parts[1]
    if isReg( r ):
      val = reg[r]
    else:
      val = int(r)

    target = i + val
    if target >= 0 and target < len(instr):
      toggle( target )

  else:
    print '! illegal instruction:', cur
    exit()

  i += 1

print reg

