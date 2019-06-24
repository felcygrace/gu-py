n,k=map(int,input().split())
l=[]
for i in range(n):
  i=int(input())
  l.append(i)
sum1=0
for n in range(0,k+1):
  sum1=sum1+n
  n=n-1
print(sum1)
