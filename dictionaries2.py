def charcount(s):
    dct = {}
    for i in s:
        if i in dct:
            dct[i] = dct[i] + 1
        else:
            dct[i] = 1
    return dct


s = input("Enter string : ")
print(charcount(s))