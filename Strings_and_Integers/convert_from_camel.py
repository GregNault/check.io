# returns a string that has no spaces but is in title case
def to_camel_case(name: str) -> str:
    str_list = name.split("_")
    new_str_list = []
    for i in str_list:
        new_str_list.append(i.title())
    new_str = "".join(new_str_list)
    
    return new_str


print("Example:")
print(to_camel_case("my_function_name"))