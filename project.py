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

def num_within(num_1, range_lo, range_hi):
    return num_1 >= range_lo and num_1 <= range_hi

print(f"Is 3 between 2 and 4 (inclusive)?: {num_within(3, 2, 4)}")
print(f"Is 3 between 1 and 3 (inclusive)?: {num_within(3, 1, 3)}")
print(f"Is 10 between 2 and 5 (inclusive)?: {num_within(10, 2, 5)}")