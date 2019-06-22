n=int(input())
temp=n
sum1=0
while temp>0:
  digit=temp%10
  sum1+=digit**3
  temp//=10
if sum1==n:
  print("yes")
else:
  print("no")
