# Multiplies each non-zero digit of an integer together and returns the product

def checkio(number: int) -> int:
    num = str(number)
    product = 1
    i = 0
    while i < len(num):
        if num[i] != "0":            
            print(product)
        i += 1
    return product


print("Example:")
print(checkio(123405))