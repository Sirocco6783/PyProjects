date = input("Enter your birthday(YYYYMMDD: ")

while len(date) >1:
    sum_digits = 0
    for digit in date:
        sum_digits += int(digit)
    date = str(sum_digits)

print(date)