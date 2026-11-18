def read_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print(f"Error: the value is not within permitted range ({min_val}..{max_val})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")

# Call the function
v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)