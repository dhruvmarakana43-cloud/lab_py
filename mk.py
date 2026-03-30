src = open("xyz.txt", "r")
data = src.read()
src.close()

dst = open("mk.txt", "w")
dst.write(data)
dst.close()
print("File copied successfully.")
