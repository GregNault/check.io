# This counts how many numbers between 1 and n are divisible by k.

def count_divisible(n: int, k: int) -> int:
    count = 0
    for num in range(n):
        if (num + 1) % k == 0:
            count += 1
    return count


print("Example:")
print(count_divisible(10000000000, 2))