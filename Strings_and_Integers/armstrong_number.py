# returns True if: The sum of each digit raised to a power equal to the length of the
# number (number of digits) it will equal the original number.

def is_armstrong(num: int) -> bool:
    num_str = str(num)
    num_list = []
    num_sum = 0
    
    # adds digits to a list
    for char in num_str:
        num_list.append(int(char))
    
    # raises each digit by power equal to length of list, sums the results of each.
    for number in num_list:
        num_sum += number ** len(num_list)

    if num == num_sum:
        return True
    
    return False



print("Example:")
print(is_armstrong(4))