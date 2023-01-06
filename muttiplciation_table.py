def multiplication_table(n):
    multiply_tbale=[]
    for i in range(n):
        multiply_tbale.append([])
    for i in range(len(multiply_tbale)):
        multiplier=i+1
        incr=1
        for j in range(n):
            res=incr*multiplier
            multiply_tbale[i].append(res)
            incr+=1
    return multiply_tbale