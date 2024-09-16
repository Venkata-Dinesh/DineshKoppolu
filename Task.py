
# Hello World Program
print("Hello World")

# Data Type Identification
x="one"
print(type(x))
a=10
print(type(a))

#String Manipulation
text="hyderbad"
z=text.upper()
print(z)
 # (2) length of string
text="hyderbad"
print(len(text))
 # (3) replace
txt="hyderbad"
c=txt.replace("hyderbad","Chenni")
print(c)

#String method exploration
k="ladakh"
vowels="aeiouAEIOU"
vowels_count=sum(1 for char in k)
i=k[::-1]
j=(k==i)
print(vowels_count)
print(i)
print(j)

#Even or Odd
l=int(input())
if l%2==0:
    print("Even")
else:
    print("Odd")

#String Concatenation
q="Welcome to"
d="Hash"
k="Include"
print(q+d+k)

#Basic List Operations
g=["dhoni","kohil","gautam","rohit"]
g.append("gaikwad")
print(g)
g.remove("gautam")
print(g)
h=sorted(g)
print(h)
h.pop()
print(h)

#Palindrome Checker
y="NOON"
x=y[::-1]
print(x)

# Simple Calculator
n=int(input())
k=int(input())
print(n+k)
print(n-k)
print(n/k)
print(n*k)