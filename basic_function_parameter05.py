# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels():
    l=["b","g" ,"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    c=0
    for d in l:
        if d in vowels:
            c+=1
    return c
print(count_vowels())


