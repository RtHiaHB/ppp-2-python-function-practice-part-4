def max_num(a, b, c):
    lister = []
    lister.append(a)
    lister.append(b)
    lister.append(c)
    greatest = 0
    for i in lister:
        if i > greatest:
            greatest = i
    return greatest

print(max_num(3, 10, 8))