try:
    my_list = [1, 2, 3]
    # This will trigger an IndexError because index 10 doesn't exist
    print(my_list[10]) 

except IndexError:
    print("Index is out of range!")

else:
    # This only runs if the try block succeeds
    print("Element found successfully!")

finally:
    # This runs no matter what
    print("Program finished.")
