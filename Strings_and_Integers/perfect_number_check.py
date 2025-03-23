# A perfect number is when the sum of a numbers factors (not including the number) equals the number
# example: 6, has factors 1, 2, 3, the sum of these is 6

def is_perfect(n: int) -> bool:
    
    factors = []
    sum = 0
    for i in range(n-1):
        if n % (i + 1) == 0:
            factors.append(i+1)

    for num in factors:
        sum += num
    
    if sum == n:
        return True
    
    return False


print("Example:")
print(is_perfect(6))