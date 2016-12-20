file = open('day20-input.txt', 'r')

blacklist = []
foo = {}
for line in file:
  line = line.rstrip()
  parts = line.split( '-' )
  a = int( parts[0] )
  b = int( parts[1] )
  
  if b <= a:
    print a, b
    exit()

  blacklist.append( (a,b) )

  if a in foo:
    print 'exists:', a
    exit()
  foo[a] = 0
  if b in foo:
    print 'exists:', b
    exit()
  foo[b] = 1

file.close()
blacklist.sort()
print blacklist

for k  in sorted(foo.iterkeys()):
  print k, foo[k]


# 0 is a lower bound
# 1 is an upper bound
0 0
1888888 1
1888889 0
1900859 0
1904062 1
2087697 1
2087698 0
2122623 1
2122624 0
2147340 0
2182652 0
2205762 0
2214508 1
2315281 1
2390846 1
2390847 0
3306156 0
5537005 1
5537006 0
8407552 0
11174641 0
13762041 1
14606952 1
14606953 0
14658906 1
15778021 1
15778022 0
16019348 1
18449276 1
19449261 1

