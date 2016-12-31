file = open('day25-input.txt', 'r')
instr = []
for line in file:
  line = line.rstrip()
  parts = line.split()
  instr.append( parts )
file.close()

def parseValue( r ):
  global reg
  if isReg( r ):
    val = reg[r]
  else:
    val = int(r)
  return val

def toggle( x ):
  cur = instr[x][0]

  if cur == 'inc':
    cmd = 'dec'
  elif cur == 'dec' or cur == 'tgl':
    cmd = 'inc'
  elif cur == 'jnz':
    cmd = 'cpy'
  elif cur == 'cpy':
    cmd = 'jnz'

  instr[x][0] = cmd

def isReg( x ):
  return x >= 'a' and x <= 'd'

pIn = 0
while True:
  print "a:", pIn, " // ",

  i = 0
  count = 0
  curClockValue = None
  reg = { 'a': pIn, 'b': 0, 'c': 0, 'd': 0 }
  while i >= 0 and i < len(instr):
    parts = instr[i]

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
      val = parseValue( lhs )
      jump = parseValue( rhs )

      if val != 0:
        i += jump
        continue

    elif cur == 'tgl': # one arg
      val = parseValue( parts[1] )
      target = i + val
      if target >= 0 and target < len(instr):
        toggle( target )

    elif cur == 'out': # one arg
      val = parseValue( parts[1] )

      if curClockValue is not None and ( ( curClockValue and val != 0 ) or \
                                         ( not curClockValue and val != 1 ) ):
        print val, " //  failed\nreg:", reg
        print
        break

      curClockValue = (val == 1)
      print val,

      count += 1
      if count % 40 == 0:
        print "\na:", pIn, "... ",

    else:
      print '! illegal instruction:', cur
      exit()

    i += 1
  pIn += 1

