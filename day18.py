
version = 'part1' # example
if version == 'example':
  pIn = '..^^.'
  pRows = 3
elif version == 'example2':
  pIn = '.^^.^.^^^^'
  pRows = 10
elif version[0:-1] == 'part':
  pIn = '.^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^'
  if version[-1] == '1':
    pRows = 40
  else:
    pRows = 400000

width = len( pIn )
rows = [ pIn ]
row = iter(rows)
count = pIn.count( '.' )

while len( rows ) < pRows:
  newRow = ''
  curRow = row.next()
  for i in range( width ):
    left = curRow[i-1] if i > 0 else '.'
    center = curRow[i]
    right = curRow[i+1] if i < width-1 else '.'

    lcr = left + center + right
    if lcr == '^^.' or lcr == '.^^' or lcr == '^..' or lcr == '..^':
      newTile = '^'
    else:
      newTile = '.'
      count += 1

    newRow += newTile

  rows.append( newRow )
  print newRow

print '\nnumber safe tiles:', count


