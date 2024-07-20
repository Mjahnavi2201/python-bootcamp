def rev(s):
    r=''
    s=s.split()
    for i in s:
        r=i+r
    return r
s=input()
print(rev(s))
'''r=''
for x in "banana":
  r=x+r
  print(r)'''