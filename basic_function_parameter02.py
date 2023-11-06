# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum():
    c = 0
    numbers=[1,2,3,4,5]
    for num in numbers:
        c += num
    return c
print(calculate_sum())
        


