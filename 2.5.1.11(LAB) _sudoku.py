#1 Reading a field
grid = []
for i in range(9):
    row = input("Enter row" + str(i+1) + ": ")
    grid.append(row)

# 2. A function to check that a string contains only the digits 1 to 9
def is_valid_block(block):
     # Convert to a list, remove duplicates using `set` and check the length
     # If the length is 9, that means there are 9 unique characters (all different)
     return len(set(block)) == 9 and len(block) == 9

valid = True

# 3. Checking the strings
for row in grid:
     if not is_valid_block(row):
          valid = False
          break

# 4. Let’s check the columns (if the rows haven’t already broken)
if valid:
     for col in range(9):
          column = []
          for row in range(9):
               column.append(grid[row][col])
          if not is_valid_block(column):
               valid = False
               break
        
# 5.Checking the 3×3 squares
if valid:
     for box_row in range(0,9,3):
          for box_col in range(0,9,3):
               square = []
               for r in range(box_row, box_row +3):
                   for c in range(box_col, box_col +3):
                       square.append(grid[r][c])
               if not is_valid_block(square):
                    valid = False
                    break
          if not valid:
               break
# 6. Conclusion
if valid:
     print("Yes")
else:
     print("No")