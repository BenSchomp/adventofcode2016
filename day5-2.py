import hashlib

#doorid = 'abc' # 05ace8e3
doorid = 'ffykfhsq'

index = 0
found = 0
password = list('________')
while found < 8:
  m = hashlib.md5()
  m.update( doorid + str(index) )
  h = m.hexdigest()
  if h[0:5] == '00000':
    pos = h[5]
    if pos >= '0' and pos < '8' and password[int(pos)] == '_':
      password[int(pos)] = h[6]
      print doorid + str(index), ''.join( password )
      found += 1
  index += 1

print "..."
print "Password:", ''.join( password )
