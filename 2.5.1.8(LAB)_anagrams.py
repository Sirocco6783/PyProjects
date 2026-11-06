text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

text1 = text1.replace(' ','').upper()
text2 = text2.replace(' ','').upper()

if sorted(text1) == sorted(text2):
    print("Anagrams.")
else:
    print("Not anagrams.")