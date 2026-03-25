"""read()"""
"""f = open("read.txt", "r")
data = f.read() # read whole file
print("File content:", data)
f.close()"""

"""read line()"""
"""f=open("read.txt", "r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("Line 1:", line1)
print("Line 2:", line2)
print("Line 3:", line3)
f.close()"""

"""read lines()"""
f = open("read.txt", "r")
lines=f.readlines()
print("List of lines:", lines)
print("Number of lines:", len(lines))
f.close()