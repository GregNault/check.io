# to take the last digit and make it the first digit in an integer
def reverse_digits(num: int) -> int:
    num_str1 = str(num)
    num_str2 = ""
    i = 1

    #if the number is negative the output is negative
    if num_str1[0] == "-":
        num_str2 += "-"
        num_str1 = num_str1[1:]

    #iterates through number and reverses order
    while i <= len(num_str1):
        num_str2 += num_str1[-i]
        i += 1
        
    return int(num_str2)


print("Example:")
print(reverse_digits(-32))