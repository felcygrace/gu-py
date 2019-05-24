a=input()
b=a.lower()
vowel="aeiou"
if a.isalpha():
  if b in vowel:
    print("vowel")
  else:
    print("consonent")
else:
  print("invalid")
