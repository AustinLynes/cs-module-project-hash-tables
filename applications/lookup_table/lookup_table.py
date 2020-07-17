# Your code here
import random
import math

# 3, 4


def slowfun_too_slow(x, y):
    # v is x**y
    # 3**4
    v = math.pow(x, y)
    # V!
    v = math.factorial(v)
    # v = v / x+y rounded
    v //= (x + y)
    # v is remander of v / x+y / 982451653
    v %= 982451653

    # return v
    return v


lookup = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    if x not in lookup:
        # v is x**y
        # 3**4
        # v = math.pow(x, y)
        # # # V!s
        # v = math.factorial(x)
        # # # v = v / x+y rounded
        # v //= (x + y)
        # # # v is remander of v / x+y / 982451653
        # v %= 982451653

        # lookup[x] = v 
        # return v
        lookup[x] = math.factorial(math.pow(x, y)) // (x + y) % 982451653

    return lookup[x]

# Do not modify below this line!


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{x},{y}: {slowfun_too_slow(x, y)}')

