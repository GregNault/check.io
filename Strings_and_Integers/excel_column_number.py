# Find the sum of each letter in the string if each place in the string is worth 26 (radix 26)
def column_number(name: str) -> int:
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_list = []
    sum = 0
    
    i = 0
    while i < len(name):
        sum += (LETTERS.index(name[i]) + 1) * (26 ** ((len(name)-1) - i))
        i += 1

    return sum

print("Example:")
print(column_number("BG"))