n = int(input())
k = int(input())
list1=[]
count=0
for num in range(0,n):
  num=int(input())
  list1.append(num)
if k in list1:
  count+=1
print(count)
