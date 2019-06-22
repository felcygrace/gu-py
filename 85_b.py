a=input()
x=''
y=''
for i in range(len(a)):
  if i%2==0:
    x=x+str(a[i])
  else:
    y=y+str(a[i])
print(str(x.strip())+' '+str(y.strip()))
