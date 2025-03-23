# returns the roots of the quadratic equation.
# not sure why we needed the iterable and union libraries, do need the math library though

from collections.abc import Iterable
from typing import Union
import math

def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    deter = (b ** 2) - (4 * a * c)
    roots = []
    print(deter)
    if deter < 0:
        return ["No real roots"]
    elif deter == 0:
        root = (-b / (2 * a))
        return [root, root]
    elif deter > 0:
        root1 = (-b - math.sqrt(deter))/(2 * a)
        root2 = (-b + math.sqrt(deter))/(2 * a)
        return[root2, root1]



print("Example:")
print(list(quadratic_roots(1, 2, 1)))