def classify_triangle(a, b, c):
    if (a > b and a > c):
        hyp = a
        s1 = b
        s2 = c
    elif (b > a and b > c):
        hyp = b
        s1 = a
        s2 = c
    else:
        hyp = c
        s1 = a
        s2 = b
    if s1**2 + s2**2 == hyp**2:
        if (a == b and b == c):
            # not possible
            return "Right Equilateral"
        elif (a == b or b == c or a == c):
            return "Right Isosceles"
        return "Right Scalene"
    else:
        if (a == b and b == c):
            return "Equilateral"
        elif (a == b or b == c or a == c):
            return "Isosceles"
        return "Scalene"
