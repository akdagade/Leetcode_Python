nums = [2]
n = 2


l = len(nums)
f = 0

if l==1 and nums[0]==n:
	del nums[0]
	exit()


while f<l-1:
	front = nums[f]
	last =  nums[l-1]
	
	if front==n and last!=n:
		nums[f] = last
		f = f+1
		l = l-1
	
	elif (last==n):
		l = l-1

	elif front!=n and last!=n:
		f = f+1	

if(nums[l-1]==n):
	l=l-1

print (str(l) + '===' + str(nums[:l])) 