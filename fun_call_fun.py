#function call another function
def check(ele):
	return ele%2==0
def increment(arr):
	count=0
	for i in arr:
		if check(i):
			print(i)
			count+=1
	return count
arr=[5,9,12,6,17,3]
print(increment(arr))