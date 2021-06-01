a=(input('Enter the String - '))
b=(input('Enter the other string -'))
c=b[0]
d=''
s=len(a)
n=a.find(c)
for i in range(0,n):
    d=d+a[i]
print('The required String is -',d)



