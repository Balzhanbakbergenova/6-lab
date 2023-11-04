#1
def get_keys_with_value_true(input_dict):
    true_keys = []
    for key, value in input_dict.items():
        if value is True:
            true_keys.append(key)
    return true_keys

# Example usage:
my_dict = {
    "a": True,
    "b": False,
    "c": True
}

result = get_keys_with_value_true(my_dict)
print(result)  # Output: ['a', 'c']





#2
def get_unique_elements(input_list):
    unique_elements = []
    seen = set()  # To keep track of elements we have seen before

    for element in input_list:
        if input_list.count(element) <= 1 and element not in seen:
            unique_elements.append(element)
            seen.add(element)

    return unique_elements

# Example usage:
my_list = [1, 2, 3, 1, 2, 4]
result = get_unique_elements(my_list)
print(result)  # Output: [3, 4]







#3
def get_date_in_format(date):
    parts = date.split(".")
    day = parts[2]
    month = parts[1]
    year = parts[0]
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date

# Example usage:
input_date = "2023.10.23"
result = get_date_in_format(input_date)
print(result)  # Output: "23.10.2023"




#4
def get_elements_with_no_more_than_two_occurrences(input_list):
    result = []
    occurrences = {}

    for element in input_list:
        if element not in occurrences:
            occurrences[element] = 1
        else:
            occurrences[element] += 1

        if occurrences[element] <= 2:
            result.append(element)

    return result

# Example usage:
my_list = [1, 2, 3, 1, 2, 4]
result = get_elements_with_no_more_than_two_occurrences(my_list)
print(result)  # Output: [1, 2]






#5
def get_words_from_string(input_string):
    words = input_string.split()
    return words

# Example usage:
my_string = "This a string with a several words."
result = get_words_from_string(my_string)
print(result)  # Output: ['This', 'a', 'string', 'with', 'a', 'several', 'words.']




#6
def get_unique_elements_with_count(input_list):
    element_count = {}
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

# Example usage:
my_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_unique_elements_with_count(my_list)
print(result)  # Output: {1: 4, 2: 3, 3: 1, 4: 1}





#7
def get_prime_numbers(n):
    is_prime = [True] * (n + 1)
    p = 2
    prime_numbers = []

    while p**2 <= n:
        if is_prime[p]:
            for i in range(p**2, n + 1, p):
                is_prime[i] = False
        p += 1

    for i in range(2, n + 1):
        if is_prime[i]:
            prime_numbers.append(i)

    return prime_numbers

# Example usage:
n = 100
result = get_prime_numbers(n)
print(result)







#8 
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers_in_list(input_list):
    prime_numbers = [num for num in input_list if is_prime(num)]
    return prime_numbers

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
result = get_prime_numbers_in_list(my_list)
print(result)  # Output: [1, 2, 3, 5, 7, 11, 13, 67, 71, 73, 83, 89]






#9
from datetime import datetime

def get_difference_between_dates(date1, date2):
    # Parse the input dates as datetime objects
    date1_obj = datetime.strptime(date1, '%Y.%m.%d')
    date2_obj = datetime.strptime(date2, '%Y.%m.%d')

    # Calculate the difference in days
    date_difference = abs((date2_obj - date1_obj).days)

    return date_difference

# Example usage:
date1 = '2023.10.23'
date2 = '2023.10.24'
result = get_difference_between_dates(date1, date2)
print(result)  # Output: 1





#10 
def get_decimal_number_from_binary_string(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

# Example usage:
binary_string = "10110011"
result = get_decimal_number_from_binary_string(binary_string)
print(result)  # Output: 43




#11 
import math

def is_perfect_square(num):
    # Check if the square root of the number is an integer
    root = math.isqrt(num)
    return root * root == num

def get_perfect_squares(input_list):
    perfect_squares = [num for num in input_list if is_perfect_square(num)]
    return perfect_squares

# Example usage:
my_list = [4, 25, 81]
result = get_perfect_squares(my_list)
print(result)  # Output: [4, 25, 81]




#12
def sort_shopping_list_by_price(shopping_list):
    sorted_list = sorted(shopping_list, key=lambda item: item['price'])
    return sorted_list

# Example usage:
shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]
result = sort_shopping_list_by_price(shopping_list)
print(result)




#13 
def get_words_starting_with_vowel(word_list):
    vowels = "aeiouAEIOU"
    vowel_words = [word for word in word_list if word[0] in vowels]
    return vowel_words

# Example usage:
word_list = ["apple", "banana", "orange", "bear", "cat"]
result = get_words_starting_with_vowel(word_list)
print(result)  # Output: ['apple', 'orange']

