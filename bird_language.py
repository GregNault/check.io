def translation(text: str) -> str:
    word_list = []
    discard_list = []
    for i in len(text):
        if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
            word_list.append(text[i])
            discard_list.append(text[1]).append(text[2])
            

    return ""


print("Example:")
print(translation("hieeelalaooo"))