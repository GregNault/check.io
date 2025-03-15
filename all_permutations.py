# Did not understand this one at all. This solution was taken from the hints
# The goal was if given a string to return a list of all possible permutations
# for example: ab -> ["ab", "ba"]

from collections.abc import Iterable

def string_permutations(s: str) -> Iterable[str]:
    if len(s) < 2: return [s]
    all = []
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i + 1:]
        for perm in string_permutations(remaining_chars):
            all.append(char + perm)
    
    return all


print("Example:")
print(list(string_permutations("abcd")))
