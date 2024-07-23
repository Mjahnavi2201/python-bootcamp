#check whether the two strings are anagram
s1='swec'
s2='cesw'
res1=sorted(s1)
res2=sorted(s2)
if len(s2)==len(s1) and res1==res2:
	print('the strings are anagram')
else:
	print('the strings are not anagram')
#s1 and s2 are anagrams
#Anagram:
#    if the characters in string s1 are also present in string s2 and length of both strings are same then they are anagram