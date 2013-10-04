
def factorial(l):
    #break 0
    # l * factorial of(l-1)
    if l == 1:
        return 1
    return l * factorial(l - 1)

# Multiply all the elements in a list
def multiply_list(l):
    if l == []:
        return 1
    return l[0] * multiply_list(l[1:])

# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) < 2:
        return l
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    return l[0:1] + reverse(l[1:-1]) + l[-1:]


# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 1 and n - 1 == 0:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return float('inf')
    elif l[0] == i:
        return 0
    return 1 + find(l[1:], i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if some_string[0] != some_string[-1]:
        return False
    elif len(some_string) <=2:
        return True
    return palindrome(some_string[1:-1])

# Given the width and height of a sheet of paper (of zero weight), and the number 
#of times to fold it,return the final dimensions of the sheet as a tuple. Assume 
#that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    elif height < width:
        width = width / 2
    else:
        height = height / 2
    return fold_paper(height, width, folds - 1)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n >= target:
        return n
    print n
    return count_up(target, n + 1)

def count_up2(n):
    if n == 0:
        print n
        return 0
    count_up2(n -1)
    print n

# def move_rings(n, e):
#     if n == 1:
#         print e.append(n)
#         return e
#     def append_up(n):
#         buffer_stick = []
#         if n == 0:
#             buffer_stick.append(n)
#         else:
#             append_up(n - 1)
#             buffer_stick.append(n)
#     buffer_stick = append_up(n)
#     n = buffer_stick[1:]
#     print e.append(move_rings(n, e))
#     return e




# def move_rings(n, e):
#     if n == 0:
#         return n
#     e.append(n)
#     b = move_rings(n-1, e)



"""start_stick = []
end_stick = []
buffer_stick = []
print move_rings(n, start_stick, end_stick, buffer_stick)"""