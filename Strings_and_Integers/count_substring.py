# This will count the number of occurances of a substring inside a string
def count_occurrences(main_str: str, sub_str: str) -> int:
    main_str = main_str.lower()
    sub_str = sub_str.lower()
    string_length = len(main_str)
    sub_length = len(sub_str)
    count = 0

    # checks each char as the starting char for the substring
    for i in range(0, string_length - sub_length + 1):
        print(main_str[i])
        if main_str[i: i + sub_length] == sub_str:
            count += 1
    return count

print(count_occurrences("Hello World hello", "hello"))
