#given an array of integers find difference of the sum of minimum and sum of maximum
#method1
num=[2,6,34,21,9,4]
sum1=sum(num)
print((sum1-min(num))-(sum1-max(num)))
#method2
num.sort()
min_sum=sum(num)-num[-1]
max_sum=sum(num)-num[0]
print(max_sum-min_sum)
#method3
min_sum=sum(num[:len(num)-1])
max_sum=sum(num[1:])
print(max_sum-min_sum)