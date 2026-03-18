# 1). square of a number

def square(no,exp=2):
    return no**exp

print(square(5))
print(square(5,3))
print(square(2,4))

# 2). 

def greet(name="Guest"):
    print("Hello ",name)
greet("Ram")
greet()

# 3).

def add(a,b=4):
    print("sum = ",a+b)

add(2)
add(2,5)