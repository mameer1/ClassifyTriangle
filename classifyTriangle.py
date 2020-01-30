def classify_triangle(*args):
    argCount = len(args)
    if argCount != 3:
        return "ERROR: Number of arguments must equal 3"
    a = args[0]
    b = args[1]
    c = args[2]
    try:
        int(a)
        int(b)
        int(c)
    except (TypeError,ValueError):
        return "ERROR: Invalid Input(s) -> non-numbers forbidden"
    if (a <= 0 or b <= 0 or c <= 0):
        return "ERROR: Invalid Input(s) -> negative numbers and zero forbidden"
    if (a + b <=c or a + c <= b or b + c <= a):
        return "ERROR: Not a triangle"
    if (a == b and b == c):
        return "The triangle is equilateral"
    if ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        if (round(a**2 + b**2, 3) == round(c**2, 3) or round(a**2 + c**2, 3) == round(b**2, 3) or round(b**2 + c**2, 3) == round(a**2, 3)):
            return "The triangle is isosceles AND right"
        else:
            return "The triangle is isosceles"
    if (a != b and b != c and c != a):
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
            return "The triangle is scalene AND right"
        else:
            return "The triangle is scalene"
    else:
        return "ERROR: hmm I'm not sure how you got here..."
