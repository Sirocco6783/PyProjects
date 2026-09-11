# ============================================
# LAB: Removing duplicate items from a list
# ============================================

# Original list with duplicates
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Let’s create a new empty list for unique items
unique_list = []

# We iterate through all the items in the original list
for item in my_list:
    # We check: if this element is not already in `unique_list`,
    # then we add it
    if item not in unique_list:
        unique_list.append(item)

# Let’s display the result
print("The list with unique elements only:")
print(unique_list)
