
version = 'part1' # example
if version == 'example':
  pIn = '..^^.'
  pRows = 3
elif version == 'example2':
  pIn = '.^^.^.^^^^'
  pRows = 10
elif version == 'part1':
  pIn = '.^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^'
  pRows = 40

width = len( pIn )
rows = [ pIn ]
row = iter(rows)

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

    newRow += newTile

  rows.append( newRow )

count = 0
for r in rows:
  count += r.count( '.' )
  print r

print '\nnumber safe tiles:', count


