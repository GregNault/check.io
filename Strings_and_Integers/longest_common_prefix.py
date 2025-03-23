
# this returns the longest common prefix for each element in the list
def longest_prefix(arr: list[str]) -> str:
    i = 0
    count = ""
    
    # sets the range of the while loop so that it won't iterate longer than the shortest element
    min_length = len(min(arr, key=len))

    # iterates through each character in each element, checks against the first element.
    while i < min_length:
        for item in arr:
            if item[i] != arr[0][i]:
                return count
        count += item[i]
        i += 1    
    return count

# These were some clear solutions given for this:

def longest_prefix(arr: list[str]) -> str:
    n, a = 0, list(zip(*arr))
    while a and len(set(a.pop(0))) == 1:
        n += 1
    return arr[0][:n]

def longest_prefix(arr: list[str]) -> str:
    # your code here
    s = arr.pop()    
    for i in range(len(s)+1):
        if not all(s[:i] in x for x in arr):
            return s[:i-1]
    return s[:i]

print("Example:")
print(repr(longest_prefix(["flower", "flow", "floght"])))

