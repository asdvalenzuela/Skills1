# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odd = []
    for number in number_list:
        if number % 2 != 0:
            odd.append(number)
    return odd

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even = []
    for number in number_list:
        if number % 2 == 0:
            even.append(number)
    return even

# Write a function that takes a list of strings and creates a new list with all strings of length 4 or greater.
def long_words(word_list):
    longer_words = []
    for word in word_list:
        if len(word) >= 4:
            longer_words.append(word)
    return longer_words
   
# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    return min(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    return max(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    divided_by_2 = []
    for number in number_list:
        divided_by_2.append(number/2.0)
    return divided_by_2

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []
    for word in word_list:
        lengths.append(len(word))
    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum_of = 0
    for number in number_list:
        sum_of += number
    return sum_of

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    product = 1
    for number in number_list:
        product *= number
    return product

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    whole_string = ""
    for word in word_list:
        whole_string = whole_string + " " + word
    return whole_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return sum_numbers(number_list)/ float(len(number_list))
