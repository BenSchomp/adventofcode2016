#file = open('day8-example.txt', 'r')
file = open('day8-input.txt', 'r')

def displayScreen( screen, w, h ):
  for y in range( h ):
    row = ''
    for x in range( w ):
      if screen[x][y] == 1:
        row += '#'
      else:
        row += '.'
    print row
  print

screen_w, screen_h = 50, 6 
screen = [[0 for x in range(screen_h)] for y in range(screen_w)]

for line in file:
  parts = line.split()
  cmd = parts[0]
  if cmd == 'rect':
    size = parts[1].split('x')
    w = int(size[0])
    h = int(size[1])
    for x in range(w):
      for y in range(h):
        screen[x][y] = 1

  elif cmd == 'rotate':
    if parts[1] == 'column':
      col = int(( parts[2].split( '=' ) )[1])
      by = int(parts[4])
      old = []
      for y in range( screen_h ):
        old.append( screen[col][y] )

      for y in range( screen_h ):
        screen[col][(y+by)%screen_h] = old[y]

    elif parts[1] == 'row':
      row = int(( parts[2].split( '=' ) )[1])
      by = int(parts[4])
      old = []
      for x in range( screen_w ):
        old.append( screen[x][row] )

      for x in range( screen_w ):
        screen[(x+by)%screen_w][row] = old[x]

  displayScreen( screen, screen_w, screen_h )

count = 0
for x in range( screen_w ):
  for y in range( screen_h ):
    count += screen[x][y]

print "Num Pixels:", count

file.close()
