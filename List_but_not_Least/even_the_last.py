# sum even elements of the array and then multiply by the last element
# empty arrays return 0

def checkio(array: list[int]) -> int:
    i = 0
    sum = 0
    ans = 0
    if array == []:
        return 0
    while i < len(array):
        sum += array[i]
        ans = sum * array[i]
        i += 2
    return ans


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))