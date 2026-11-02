def mysplit(strng):
    result = []
    word = ""
    for char in strng:
        if char != " ":
            word += char
        if char == " " and word != "":
            result.append(word)
            word = ""
    if word != "":
        result.append(word)
    return result               


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
