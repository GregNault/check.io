# Returns the most common lower case letter found in the string

def checkio(text: str) -> str:
    text = text.lower()
    count = 0
    letter = ""
    
    for char in text:
        num = text.count(char)
        # the ord() method returns the ascii value of the character
        if ord(char) <= 96 or ord(char) >= 123:
            continue
        if num > count:
            count = num
            letter = char
        elif num == count and char < letter:
            letter = char
    return letter


print("Example:")
print(checkio("AAaooo!!!!"))
