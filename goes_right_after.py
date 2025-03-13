# Returns true if in the sting there are two characters where the first character preceeds the second.
def goes_after(word: str, first: str, second: str) -> bool:
    index_list = []
    if word.count(first) == 0:
        return False
    ind1 = word.index(first)
    try:
        if word[ind1 + 1] == second:
            return True
    except:
        return False
    return False


print("Example:")
print(goes_after("world", "w", "o"))
print(goes_after("plnorlma", "a", "n"))
print(goes_after("Almaz", "m", "a"))