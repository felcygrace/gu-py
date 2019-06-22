
n=int(input())
k=int(input())
a=n*k
root=a**0.5
if int(root + 0.5) ** 2 == a:
    print("yes")
else:
    print("no")
