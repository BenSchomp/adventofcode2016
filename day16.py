version = 'part1' # 'example'
if version == 'example':
  pIn = '10000'
  pLen = 20
elif version == 'part1':
  pIn = '00101000101111010'
  pLen = 272

def dragon( s ):
  reverse = ''
  
  for i in range( len(s)-1, -1, -1 ):
    if s[i] == '0':
      reverse += '1'
    else:
      reverse += '0'

  return s + '0' + reverse

def getChecksum( source ):
  s = source
  while len( s ) % 2 == 0:
    chksm = ''
    for i in range( 0, len(s), 2 ):
      #print i, s[i], s[i+1]
      if s[i] == s[i+1]:
        chksm += '1'
      else:
        chksm += '0'
    s = chksm

  return chksm
     

data = pIn
#print data, len( data )
while len( data ) < pLen:
  data = dragon( data )
  #print data, len( data )

data = data[0:pLen]
print "data:", data

checksum = getChecksum( data )
print "checksum:", checksum

