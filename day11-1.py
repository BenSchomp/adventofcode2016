from copy import deepcopy
from collections import deque
  
class Node:
  nodes = dict()

  #def __init__( self, floors, elevator ):
  def __init__( self, orig=None ):
    self.floors = []
    self.elevator = 0

    self.parentId = -1
    self.distance = 0
    self.color = 0

    if( orig != None ):
      self.copy_ctor( orig )

  def copy_ctor( self, orig ):
    self.floors = deepcopy( orig.floors )
    self.elevator = orig.elevator
    self.parentId = id( orig )
    self.distance = orig.distance + 1

  def key( self ):
    result = '|'
    for floor in self.floors:
      result += ''.join( floor ) + '|'
    result += '-' + str( self.elevator )
    return result

  def isSolved( self ):
    return len( self.floors[0] ) + len( self.floors[1] ) + len( self.floors[2] ) == 0

  def isFried( self ):
    # match up microchips with generators
    chips = []
    generators = []
    for i in self.floors[ self.elevator ]:
      if i[1] == 'M':
        chips.append( i )
      elif i[1] == 'G':
        generators.append( i )
      else:
        exit()

    matches = 0
    for i in chips:
      for j in generators:
        if i[0] == j[0]:
          matches += 1
          break

    if len( generators ) > matches and len( chips ) > matches:
      #print ' ! fried', self.floors[ self.elevator ], '!'
      return True
    else:
      return False

  def setFloors( self, newFloors ):
    self.floors = newFloors
    for i in self.floors:
      i.sort()

    self.markSeen()

  # returns False if it was previously seen, or fries chips
  def markSeen( self ):
    if self.key() in self.nodes:
      #print ' ! already seen it !'
      return False
    self.nodes[ self.key() ] = self

    if self.isFried():
      return False

    self.nodes[id(self)] = self
    return True

  # returns False if the new position is invalid
  def move( self, items, to ):
    if abs( self.elevator - to ) != 1:
      print ' ! illegal move!'
      return False

    for i in items:
      self.floors[self.elevator].remove( i )
      self.floors[to].append( i )

    self.floors[to].sort()
    self.elevator = to

    # check solved
    if self.isSolved():
      print "** solved: %d steps **" % self.distance
      i = self
      while i.parentId != -1:
        print i.key()
        #i.display()
        i = self.nodes[i.parentId]
      #i.display()
      print i.key()
      exit()

    return self.markSeen()

  def display( self, text = '' ):
    print
    if text != '':
      print text
    print "Id: %d, Key: %s" % (id(self), self.key())
    for i in range( 3, -1, -1 ):
      print 'f%d:' % (i+1),
      print '*' if self.elevator == i else ' ',
      print ' '.join( self.floors[i] )

file = open('day11-input.txt', 'r')

# initial setup
floors =[ [] for i in range(0, 4) ]
i = 0
for line in file:
  line = line.rstrip()

  parts = line.split( ' a ' )
  for part in parts[1:]:
    subParts = part.split()
    if subParts[1][0:9] == 'generator':
      code = subParts[0][0] + 'g'
    elif subParts[1][0:9] == 'microchip':
      code = subParts[0][0] + 'm'

    floors[i].append( code.upper() )
    floors[i].sort()
  i += 1

file.close()

work = deque() # queue to hold all current level of working nodes

# create root node
root = Node()
root.setFloors( floors )
work.append( root )
print "\n---- ROOT (id: %d, #work: %d, dist: %d) ----" \
  % ( id(root), len( work ), 0 )
root.display()

# do it
while len( work ) > 0:
  parent = work.popleft()
  print "\n---- New Parent (id: %d, #work: %d, dist: %d) ----" \
    % ( id(parent), len( work ), parent.distance + 1 )

  curElevator = parent.elevator
  curFloor = parent.floors[ curElevator ]
  numItems = len( curFloor )

  # try moving each piece up and then down and both dirs in pairs
  for i in range( 0, numItems ):
    # up
    if curElevator < 3:
      newNode = Node( parent )
      if newNode.move( [ curFloor[i] ], curElevator + 1 ):
        work.append( newNode )

    #down
    if curElevator > 0:
      newNode = Node( parent )
      if newNode.move( [ curFloor[i] ], curElevator - 1 ):
        work.append( newNode )

  for i in range( 0, numItems ):
    for j in range( i+1, numItems ):
      # up
      if curElevator < 3:
        newNode = Node( parent )
        if newNode.move( [ curFloor[i], curFloor[j] ], curElevator + 1 ):
          work.append( newNode )

      #down
      if curElevator > 0:
        newNode = Node( parent )
        if newNode.move( [ curFloor[i], curFloor[j] ], curElevator - 1 ):
          work.append( newNode )


