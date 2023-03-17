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

def pascal(n):
    triangle = [[1], [1, 1]]
    #base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        #fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            #create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev) + 1
            for i in range(length):
                #first number is 1
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number -1][i - 1] + triangle[row_number-1][i])
                #last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

print(f"row 2 in Pascal's triangle:")
pascal(2)
print(f"row 5 in Pascal's triangle:")
pascal(5)