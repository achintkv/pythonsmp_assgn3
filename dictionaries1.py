dict1={

}
dict2={

}
dict3={

}
n=int(input('Enter the no of items in dict1 -'))
m=int(input('Enter the no of items in dict2 -'))
for i in range(0,n):
     dict1[input('key-')]=int(input('value-'))
for i in range(0,m):
     dict2[input('key-')]=int(input('value-'))

for key in dict1:
    if key in dict2:
        dict3[key]=dict1[key]+dict2[key]
    else:
        if key in dict1:
            dict3[key]=dict1[key]
for key in dict2:
    if key not in dict3:
        dict3[key]=dict2[key]
print('dict1 -',dict1)
print('dict2 -',dict2)
print('The required dictionary is -',dict3)

        


