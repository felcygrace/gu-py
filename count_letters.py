a=input()
count=0
for i in range(len(a)):
  if a[i].isalpha():
    count+=1
print(count)
