# sorts a list of integers and then returns the average of the middle two elements, or the middle element.

def median(data: list[int]) -> int | float:
    mid = len(data) / 2
    if len(data) % 2 == 0:
        avg_median = (data[int(mid-1)] + data[int(mid)])/2
        return avg_median
    else:
        return data[int(mid)]


def checkio(data: list[int]) -> int | float:
    lowest_char = 0
    sort_list = []
    min_length = len(data)
    i = 0

    while i < min_length:
        lowest_char = min(data)
        data.remove(lowest_char)
        sort_list.append(lowest_char)
        i += 1

    return median(sort_list)


print("Example:")
print(checkio([1, 2, 3, 4, 5, 6]))