# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    return filter(lambda x: x % 2 != 0,number_list)
   
# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    return filter(lambda x: x % 2 == 0, number_list)

# Write a function that takes a list of strings and creates a new list with all strings of length 4 or greater.
def long_words(word_list):
    return filter(lambda x : len(x) >= 4, word_list)
   
# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    return reduce(lambda x,y: min(x,y), number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    return reduce(lambda x,y: max(x,y), number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    return map(lambda x: x/2.0, number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return map(lambda x: len(x), word_list)
    
# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    return reduce(lambda x,y: x+y, number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return reduce(lambda x,y: x*y, number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return reduce(lambda x,y: x+" "+y, word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list)/ float(len(number_list))
