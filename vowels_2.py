a=input()
b=0
vowels = ["a", "e", "i", "o", "u"]
for i in vowels:
  if i in a:
    b= True
if b==True:
    print("yes")
else:
    print("no")
