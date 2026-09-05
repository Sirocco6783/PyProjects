c0 = int(input("Enter a natural number: "))

steps = 0  # Count steps

while c0 != 1:
    # First, we display the current value (as required by the task)
    print(c0)
    
    # Checking accuracy
    if c0 % 2 == 0:
        c0 = c0 + 2   # According to the problem statement
    else:
        c0 = 3 * c0 + 1
    
    steps += 1  # Increase the counter

# When the loop is finished, we print the last value (it should be 1)
print(c0)
print("steps =", steps)