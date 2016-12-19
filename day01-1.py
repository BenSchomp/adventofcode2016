commands = [ "R5","R4","R2","L3","R1","R1","L4","L5","R3","L1","L1","R4","L2","R1","R4","R4","L2","L2","R4","L4","R1","R3","L3","L1","L2","R1","R5","L5","L1","L1","R3","R5","L1","R4","L5","R5","R1","L185","R4","L1","R51","R3","L2","R78","R1","L4","R188","R1","L5","R5","R2","R3","L5","R3","R4","L1","R2","R2","L4","L4","L5","R5","R4","L4","R2","L5","R2","L1","L4","R4","L4","R2","L3","L4","R2","L3","R3","R2","L2","L3","R4","R3","R1","L4","L2","L5","R4","R4","L1","R1","L5","L1","R3","R1","L2","R1","R1","R3","L4","L1","L3","R2","R4","R2","L2","R1","L5","R3","L3","R3","L1","R4","L3","L3","R4","L2","L1","L3","R2","R3","L2","L1","R4","L3","L5","L2","L4","R1","L4","L4","R3","R5","L4","L1","L1","R4","L2","R5","R1","R1","R2","R1","R5","L1","L3","L5","R2" ]

def getNewPosition( x, y, heading, distance ):
  if heading == 0:
    y += distance
  elif heading == 1:
    x += distance
  elif heading == 2: 
    y -= distance
  else:
    x -= distance
      
  return ( x, y )
      
x = 0
y = 0 
heading = 0
      
for command in commands:
  rotate = command[0]
  distance = int( command[1:] )
  if command[0] == 'R':
    heading = 0 if heading == 3 else heading + 1
  else:
    heading = 3 if heading == 0 else heading - 1
    
  (x, y) = getNewPosition( x, y, heading, distance )
  
print ("%d blocks" % ( abs(x) + abs(y) ) )
