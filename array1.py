#1)
from array import array
arr = array('i',[10,20,30,40,50])
print(len(arr))

#2)
arr = array('i',[10,20,30,40,50])
arr.append(40)
print(len(arr))

#3)
arr =array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#4)
arr =array('i',[10,20,40])
arr.remove(20)
print(arr)

#5)
arr =array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)