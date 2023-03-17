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

print(f"Max of 3, 10, and 8: {max_num(3, 10, 8)}")

def mult_list(*args):
    product = 1
    for i in args:
        product = product * i
    return product

print(f"Product of 3, 8, and 10: {mult_list(3, 8, 10)}")

def rev_string(my_str):
    reversed = ""
    for i in range(len(my_str) - 1, -1, -1):
        reversed =  reversed + my_str[i]
    return reversed

print(f"'Thomas' reversed: {rev_string('Thomas')}")
