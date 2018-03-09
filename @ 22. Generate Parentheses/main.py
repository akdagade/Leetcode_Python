class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
        	return []

        if n==1:
        	return ['()']

        tmp = self.generateParenthesis(n-1)
        retList = list()

        for ele in tmp:
        	t = '(' + ele + ')'
        	if t not in retList:
        		retList.append('(' + ele + ')')
        	ln = len(ele)
        	for i in range(ln+1):
        		t = ele[:i] + '()' + ele[i:]
        		if t not in retList:
        			retList.append(t)	

        return retList
'''
import sys
n=int(sys.argv[1])

brk = []
brk.append([])
if n==0:
	print([])
	exit()

brk.append(['()'])
if n==1:
	print(brk[1])
	exit()

brk.append(['()()','(())'])
if n==2:
	print(brk[2])
	exit()

for i in range(3,n+1):
	half = int(i/2) if i%2==0 else int(i/2)+1
	tmpList = list()
	for j in range(half,i):
		for b2 in brk[j]:
			b2len= len(b2)
			for b1 in brk[i-j]:
				b1len= len(b1)
				
				tmp = b1+b2
				if tmp not in tmpList:
					tmpList.append(tmp)
				
				tmp = b2+b1
				if tmp not in tmpList:
					tmpList.append(tmp)
				
				tmp = b2[:int(b2len/2)] + b1 + b2[int(b2len/2):]
				if tmp not in tmpList:
					tmpList.append(tmp)

				tmp = b1[:int(b1len/2)] + b2 + b1[int(b1len/2):]
				if tmp not in tmpList:
					tmpList.append(tmp)
		#print(tmpList)
	brk.append(tmpList)

new = list()

for ele in brk[3]:
	tmp = ele + '()'
	if tmp not in new:
		new.append(tmp)
	
	tmp = '()' + ele 
	if tmp not in new:
		new.append(tmp)
	
	for t in range(1,4):
		tmp = ele[:t] + '()' + ele[t:]
		if tmp not in new:
			new.append(tmp)

	tmp = '(' + b2 + ')'
	if tmp not in new:
		new.append(tmp)


print("Total combinations new: " + str(len(new)))
for l in new:
	print(l)

print("Total combinations : " + str(len(brk[n])))
for l in brk[n]:
	print(l)
'''