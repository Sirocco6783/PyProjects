# Step 1: create an empty list
beatles = []
print("Step 1:", beatles)

# Step 2: use append() to add John Lennon, Paul McCartney, George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3: use a for loop and append() to ask the user to add Stu Sutcliffe and Pete Best
for i in range(2):
    name = input("Enter a member to add: ")
    beatles.append(name)
print("Step 3:", beatles)

# Step 4: use del to remove Stu Sutcliffe and Pete Best
# They are the last two elements, so we can remove by index
# Alternative: use remove() if you know the exact values, but here we use del
del beatles[-1]   # removes Pete Best (last)
del beatles[-1]   # now removes Stu Sutcliffe (new last)
print("Step 4:", beatles)

# Step 5: use insert() to add Ringo Starr to the beginning
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))