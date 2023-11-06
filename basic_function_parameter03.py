# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest():
    l=[1,2,3,4,5]
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min
print(find_smallest())
