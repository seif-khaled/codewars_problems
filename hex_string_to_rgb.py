def hex_string_to_RGB(t): 

	if type(t)==int:
		print("invalid input")
	elif len(t)>7or len(t)<7:
		print("length is invalid")
	else:
		d={}
		flag=0
		t=t.lower()
		for i in t:
				if i.isalpha():
						flag=1
						break
		if flag==1:
			c=[]
			indx=[]
			for i in range(len(t)):
						if t[i]=='a':
							c.append(10)
							indx.append(i)
						elif t[i]=='b':
							c.append(11)
							indx.append(i)
						elif t[i]=='c':
							c.append(12)
							indx.append(i)	
						elif t[i]=='d':
							c.append(13)
							indx.append(i)
						elif t[i]=='e':
							c.append(14)
							indx.append(i)
						elif t[i]=='f':
							c.append(15)
							indx.append(i)
						else:
							c.append(t[i])
			d['r']=(int(c[1])*16)+(int(c[2])*1)
			d['g']=(int(c[3])*16)+(int(c[4])*1)
			d['b']=(int(c[5])*16)+(int(c[6])*1)
			return d
		else:
			d['r']=(int(t[1])*16)+(int(t[2])*1)
			d['g']=(int(t[3])*16)+(int(t[4])*1)
			d['b']=(int(t[5])*16)+(int(t[6])*1)
		return d