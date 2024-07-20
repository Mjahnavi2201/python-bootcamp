#Day3 Task-2:
'''
PASSWORD VALIDATION: 
-You are given a string S, check whether the string is valid password or not.
-Password is "Valid" if the string satisfies the below conditions else the string is "Invalid"
-Use check function
 
Conditions:-	
-Length(password)>8
-Password should contain atleast
	->1 capital letter
	->1 small letter
	->1 digit
	->1 special character

Input Format:-
-Take a string S as input

Sample Input:-
S='Excellence@#$%'

Sample Output:-
Invalid
'''
def check(s):
    #special_char=['!','@','#','$','%','^','&','*','`','?']
    up_c,low_c,sp_c,dig_c=0,0,0,0
    if len(s)>8:
        for i in range(len(s)):
            if s[i].isdigit():
                dig_c+=1
            elif s[i].isupper():
                up_c+=1
            elif s[i].islower():
                low_c+=1
            elif s[i].isascii():
                sp_c+=1   
            else:
                break
        if dig_c>0 and up_c>0 and low_c>0 and sp_c>0:
            print("Valid")
        else:
            print("Invalid")                
    else:    
        print("Invalid")
string=input()
check(string)    