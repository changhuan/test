#!/uer/bin/python
def searchNum(array):
	if len(array)==1:
	   return 0
	s=len(array)
	i=1
	count=0
	for i<s:
	   for j< i:
	       if array[j]<array[i]:
	           count++
	           j++
	       else:
	           j++
           j=0
	   i++
	return count

	 
	          
	      
