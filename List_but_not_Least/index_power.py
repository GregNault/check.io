# takes the int at index n and raises it to the nth power
# if index out of range return -1
def index_power2(ar: list[int], n: int) -> int:
    if n > len(ar)-1:
        return -1
    return ar[n] ** n
    
# second attempt but using error handling:
def index_power(ar: list[int], n: int) -> int:
    try:
        return ar[n] ** n
    except IndexError:
        return -1
 
print("Example:")
print(index_power([96, 92, 94], 3))