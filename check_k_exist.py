n = int(input())
k = int(input())
list1=[]
for num in range(0,n):
  num=int(input())
  list1.append(num)
if k in list1:
  print("yes")
else:
  print("no")
