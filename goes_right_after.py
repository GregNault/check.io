def goes_after(word: str, first: str, second: str) -> bool:
    index_list = []
    if word.count(first) == 0:
        return False
    if word.endswith(first) == True:
        return False
    
    ind1 = word.index(first)
    if word[ind1 + 1] == second:
        return True
    return False


print("Example:")
print(goes_after("world", "w", "o"))
print(goes_after("panorama", "a", "n"))