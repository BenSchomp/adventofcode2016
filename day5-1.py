import hashlib

#doorid = 'abc' # 18f47a30
doorid = 'ffykfhsq'

index = 0
password = ''
while len( password ) < 8:
  m = hashlib.md5()
  m.update( doorid + str(index) )
  h = m.hexdigest()
  if h[0:5] == '00000':
    password += h[5]
    print doorid + str(index), password
  index += 1

print "Password:", password
