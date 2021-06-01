
dict1={
    
}
dict2={
    
}
reqdict={

}
n=int(input('Enter the No of keys in Dict1-'))
m=int(input('Enter the No of keys in Dict2-'))
keys1=[]
keys2=[]
values1=[]
values2=[]
for i in range(0,n):
    keys1.append(input('Enter the key of dict1-'))
    values1.append(int(input('Enter the corresponding value -')))
    dict1[keys1[i]]=values1[i]
    
for i in range(0,m):
    keys2.append(input('Enter the key of dict2-'))
    values2.append(int(input('Enter the corresponding value -')))
    dict2[keys2[i]]=values2[i]
print('Dict1 - ',dict1)
print('Dict2 is - ',dict2)

for i in range(0,n-1):
    for j in range(0,m-1):
        if keys1[i]==keys2[j]:
            keys2.pop(j)
            values1[i]=values1[i]+values2[j]
            values2.pop(j)
            m=m-1
for i in range(0,n):
    reqdict[keys1[i]]=values1[i]
for i in range(0,m):
    reqdict[keys2[i]]=values2[i]
print('The required dictionary is ',reqdict)

    






    

