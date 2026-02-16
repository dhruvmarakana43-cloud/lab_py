fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")
for i in range(3):
    print(f"Iteration number: {i}")

count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Crucial: update the condition to avoid an infinite loop


# A loop within a loop
adj = ["red", "tasty"]
fruits = ["apple", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for i in range (1,11):
    print("5 x",i,"=",5*i)
    
    
for i in range (1,11):
    print(i)
    
    
for i in range (1,55):
    if i % 2 == 0:
        print(i)

for i in range (1,55):
    if i % 2 != 0:
        print(i)
    
name="atmiya"
for letter in name:
    print(letter)
    
total = 0 
for i in range(1,10):
    total = total + i
    print("sum is :",total)
    
numbers = [10,20,30,40,50]
for n in numbers:
    print(n)
    
for i in range(3):
    print("hello")