hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print("Initial list:", hat_list)


hat_list[2] = 1 # Step 1: write a line of code that prompts the user
print("List after replacing the middle number:", hat_list) # to replace the middle number with an integer number entered by the user.
print("Length of the list after replacement:", len(hat_list)) # Step 3: write a line of code that prints the length of the existing list.

del hat_list[4] # Step 2: write a line of code that removes the last element from the list.
print("List after removing the last element:", hat_list) # Step 3: write a line of code that prints the length of the existing list.
print("Length of the list after removing the last element:", len(hat_list)) # Step 3: write a line of code that prints the length of the existing list.

print(hat_list)
