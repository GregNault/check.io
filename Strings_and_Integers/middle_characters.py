# returns the middle character for odd strings, middle two characters for even strings

def middle(text: str) -> str:
    length = len(text)
    mid_char = ""
    if length % 2 == 0:
        mid_char = text[int(length/2)-1] + text[int(length/2)]
    else:
        mid_char = text[int(length/2)]
    return mid_char


print("Example:")
print(middle("example"))
            