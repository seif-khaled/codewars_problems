def productFib(n):

	x=[0,1]
	result=[]
	flag=0
	index_1=0
	index_2=1
	while flag==0 :
		x.append((x[index_1]+x[index_2]))
		product=x[index_1]*x[index_2]
		if product>n:
			break
		#print(product)
		if product==n:	
			result.append(x[index_1]) 
			result.append(x[index_2])
			result.append(True)
			flag=1
			return result
		index_1+=1
		index_2+=1
	if flag==0:
			result.append(x[index_1]) 
			result.append(x[index_2])
			result.append(False)
			return result