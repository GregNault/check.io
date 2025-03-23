# returns a string that has inserted spaces between words and made all lower case.

def from_camel_case(name: str) -> str:
    str_list = []

    for char in name:
        if char.isupper():
            str_list.append("_")
            str_list.append(char)
        elif char.islower():
            str_list.append(char)
    str_list.remove("_")
    new_string = "".join(str_list)
    
    return new_string.lower()

        


print("Example:")
print(from_camel_case("MyFunctionName"))