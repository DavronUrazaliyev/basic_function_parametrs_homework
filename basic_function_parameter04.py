# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average():
    l=[1,2,3,4,5]
    s=0
    average=0
    a=len(l)
    for i in l:
        s+=i
        average=s/a
    return average
print(calculate_average())
        
        