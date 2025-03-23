# add another zero to the list for every zero.

from collections.abc import Iterable

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    new_list = []
    for item in donuts:
        if item == 0:
            new_list.append(0)
        new_list.append(item)
    return new_list

print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))