# returns whichever true or false occurs more
# if tie or if list is empty return false

def is_majority(items: list[bool]) -> bool:
    t = 0
    f = 0
    for item in items:
        if item == True:
            t += 1
        elif item == False:
            f += 1
    if t > f:
        return True
    return False


print("Example:")
print(is_majority([True, True, False, True, False, False]))