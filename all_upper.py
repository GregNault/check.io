# Returns true if each char in string is upper case or a number.
def is_all_upper(text: str) -> bool:
    i = 0
    while i < len(text): 
        if ord(text[i]) <= 64 or ord(text[i]) >= 91:
            if text[i] == " " or ord(text[i]) >= 48 and ord(text[i]) <= 57:
                i += 1
                continue
            return False
        i += 1
    return True


print("Example:")
print(is_all_upper("ALL UPPER"))