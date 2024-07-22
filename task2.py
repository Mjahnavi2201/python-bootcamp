'''
Count Halindrome
-the string should be palindrome
-if string is not palindrome:
	->divide the string into 2 equal parts
	->check if any substring is palindrome
	->if atleast one substring is palindrome then the string is Halindrome
-count all halindromes
'''
l1=['aba','sasdad','aaaccc','tapdog','emepe']
count=0
for i in l1:
    rev=i[::-1]
    if rev==i:
        count+=1
    else:
        n=(len(i)-1)//2
        sub_str1=i[:n+1:]
        sub_str2=i[n::]
        rev=sub_str1[::-1]
        if rev==sub_str1:
            count+=1
        else:
            rev=sub_str2[::-1]
            if rev==sub_str2:
                count+=1
print(count)