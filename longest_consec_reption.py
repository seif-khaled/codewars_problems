def longest_repetition(string):
    arr=[]
    num=[]
    chars=[]
    z=0
    flag=0
    counter=0
    switch = 0
    c=""
    l=0
    max=-54877812
    if(string==""):
        return c,l
    else:
        for letter in range(len(string)):
            if (letter == len(string) - 1):
                break
            if (string[letter] == string[letter + 1]):
                switch = 1
                break
        if (switch == 1):
            for i in range(0, len(string)):
                if (counter > 0):
                    counter -= 1
                    continue
                if (i == len(string) - 1):
                    break
                if (string[i] == string[i + 1]):
                    # chars[z]=string[i]
                    # counter=1
                    chars.append(string[i])
                    for j in range(i, len(string)):
                        if (flag == 1):
                            flag = 0
                            continue
                        if (j == len(string) - 1 and string[j] == chars[z]):
                            arr.append(string[j])
                            num.append(len(arr))
                            counter = len(arr) - 1
                            break
                        elif (j == len(string) - 1 and string[j] != chars[z]):
                            # arr.append(string[j])
                            num.append(len(arr))
                            counter = len(arr) - 1
                            break
                        elif (string[j] == string[j + 1] and string[j] == chars[z]):
                            if (j == len(string) - 2):
                                arr.append(string[j])
                                arr.append(string[j + 1])
                                num.append(len(arr))
                                counter = len(arr) - 1
                                arr = []
                                break
                            else:
                                arr.append(string[j])
                                arr.append(string[j + 1])
                                flag = 1
                            # counter+=1
                        elif (string[j] != string[j + 1] and string[j] == chars[z]):
                            arr.append(string[j])
                            # counter+=1
                        elif (string[j] != string[j + 1] and string[j] != chars[z]):
                            num.append(len(arr))
                            counter = len(arr) - 1
                            arr = []
                            z += 1
                            break
                        elif (string[j] == string[j + 1] and string[j] != chars[z]):
                            num.append(len(arr))
                            counter = len(arr) - 1
                            arr = []
                            z += 1
                            break
            for number in range(len(num)):
                if(num[number]>max):
                    max=num[number]
                    index=number
            return chars[index], max
        elif (switch == 0):
            c = string[0]
            l = 1
            return c, l