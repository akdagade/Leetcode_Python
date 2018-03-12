"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


haystack = "hell3r23rr3eacwvvo"
needle = "23"

hl = len(haystack)
nl = len(needle)

for i in range(hl):
	if hl-i<nl:
		print (-1)
	c = i
	flag = 0
	for n in needle:
		if(n!=haystack[c]):
			flag=1
			break
		c = c + 1	
	if(flag==0):
		print(i)