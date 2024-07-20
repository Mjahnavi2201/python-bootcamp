def rev(s):
    s=s.split()
    for i in s:
        r=i[::-1]
        print(r,end=" ")
s=input() #hi hello how are u
rev(s)