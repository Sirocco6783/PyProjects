word = input("Enter a word: ").lower()
string = input("Enter a string: ").lower()

start = 0
found = True

for char in word:
    idx = string.find(char, start)
    if idx == -1:
        found = False
        break
    start = idx +1

if found:
    print("Yes")
else:
    print("No")