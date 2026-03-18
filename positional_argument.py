# 1). basic positonal argument

def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,4)
print("sum=",result)

# 2). student information

def student_info(name, roll, marks):
    print("Name : ",name)
    print("Roll No : ",roll)
    print("Marks : ",marks)

student_info("Ram",100,85)

# 3). simple interest

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interst : ",si)
simple_interest(1000,2,3)
simple_interest(4000,4.5,3)

# 4). area of circle

def area_circle(r):
    area_circle=3.14*r*r
    print("area of circle : ",area_circle)
area_circle(5)
area_circle(9.3)

# 5). check number positive negative or zero

def check_value(no):
    if(no>0):
        print("Positive")
    elif(no<0):
        print("Negative")
    else:
        print("Zero")
check_value(12)
check_value(-10)
check_value(0)

# 6). odd or even

def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
odd_even(24)
odd_even(11)

# 7). arithmetic operation

def addition(a,b):
    add=a+b
    print("Addition of two values : ",add)
addition(2,22)