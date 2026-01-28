Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#assignment operator
x=10
print(x)
10
#urnary minus
a=5
print(-a)
-5
#relational
p=10
q=5
print(p>q)
True
print(p==q)
False
#logical
x=true
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x=true
a=true
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
d=true
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
d='true'
f='false'
print(d and f)
false
print(d or f)
true
print(not d)
False
#boolean
is_pass=true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    is_pass=true
NameError: name 'true' is not defined. Did you mean: 'True'?
is_pass=True
print(is_pass)
True
#bitwise
a=5
b=3
print(a & b)
1
print(a | b)
7
#membership
numbers=[1,2,3,4,5]
print(2 in numbers)
True
print(6 not  in numbers)
True
#identity
x=10
y=10
print(x is y)
True
print(x is not y)
False

