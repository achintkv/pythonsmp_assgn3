def arecount(s):
    lst = s.split(' ')
    count = 0
    for i in range(0,len(lst)):
        if(lst[i] == 'are'):
            count = count + 1
    return count


s = input("Enter string : ")
print(arecount(s))