# returns the number of zeroes at the end of the number

def end_zeros(a: int) -> int:
    a = str(a)
    count = 0
    for i, num in enumerate(a, start=1):
        if a[-i] == "0":
            count += 1
        else:
            return count
    return count


print("Example:")
print(end_zeros(1001000))