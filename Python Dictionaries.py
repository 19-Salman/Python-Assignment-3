#Basic Operations
#1.Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
student={
    "name":"Salman",
    "age":"19",
    "grade":"A"}
#2.Access the value of the key grade in the student dictionary.
student_grade=student["grade"]
print(student_grade)
#3.Add a new key city to the student dictionary and set its value to "New York".
student["city"]="Faisalabad"
#4.Update the value of the age key in the student dictionary to 20.
student["age"]="20"
#5.Remove the key city from the student dictionary.
del student["city"]
#Iterating through dictionaries
# 6.Iterate through the dictionary student and print all keys.
for each_key in student.keys():
    print(each_key) 
#7.Iterate through the dictionary student and print all values.
for each_value in student.values():
    print(each_value)
#8.Iterate through the dictionary student and print all key-value pairs in the format key: value.
for each_key, each_value in student.items():
    print(each_key+":"+each_value)
#9.Check if the key grade exists in the student dictionary and print True or False.
if student.keys() and student["grade"]:
    print("true")
else:
    print("false")
#10.Count the total number of keys in the student dictionary.
key_nums=len(student.keys())
print(key_nums)
#11.Merge the following two dictionaries and print the result.
dict1 = {'a': 1, 'b':2}  
dict2 = {'c':3, 'd':4}  
dict1.update(dict2)           #using update method
merge_dict={**dict1,**dict2}
print(merge_dict)
#12Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
list_of_tuples=[('name', "Alice"), ('age', 25), ('city', "Paris")]
result_dict=dict(list_of_tuples)  #using dict() operation
print(result_dict)
#13.Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
# Original dictionary
my_dict = {'z': 1, 'a': 2, 'c': 3}

# Sort the keys in ascending order
sorted_dict = {k: my_dict[k] for k in sorted(my_dict.keys())}

# Print the sorted dictionary
print(sorted_dict)
#14.Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Reverse the dictionary (keys become values and values become keys)
reversed_dict = {v: k for k, v in my_dict.items()}

# Print the reversed dictionary
print(reversed_dict)
#15.Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
def are_dicts_identical(dict1, dict2):
    return dict1 == dict2

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'a': 1, 'b': 3, 'c': 2}

# Test the function
print(are_dicts_identical(dict1, dict2))  # Output: True
print(are_dicts_identical(dict1, dict3))  # Output: False
#Nested Dictionaries
#Create a nested dictionary to represent the following data:
#Person:  
  #Name: John  
  #Age: 30  
 # Address:  
    #Street: 123 Elm St  
   # City: Boston 
   # Nested dictionary representing the data
person = {
    'Name': 'John',
    'Age': 30,
    'Address': {
        'Street': '123 Elm St',
        'City': 'Boston'
    }
}

# Print the nested dictionary
print(person)
#17.Access the value of the City key in the nested dictionary from the previous question.

# Access the value of the 'City' key
city = person['Address']['City']

# Print the value
print(city)
#18.Add a new key Phone to the nested dictionary with the value "123-456-7890".

# Add a new key 'Phone' to the main dictionary
person['Phone'] = '123-456-7890'

# Print the updated dictionary
print(person)
#19.Delete the Address key from the nested dictionary.
# Delete the 'Address' key from the nested dictionary
del person['Address']

# Print the updated dictionary
print(person)
#20.Iterate through all the keys in the outermost level of the nested dictionary and print them.
# Iterate through the outermost keys and print them
for key in person.keys():
    print(key)
#Applications of Dictionaries
#21.Use a dictionary to count the occurrences of each word in the string "hello world hello python world".
# Input string
sentence = "hello world hello python world"

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Iterate over each word in the list of words
for word in words:
    if word in word_count:
        word_count[word] += 1  # Increment count if word is already in dictionary
    else:
        word_count[word] = 1   # Initialize count if word is not in dictionary

# Print the word count dictionary
print(word_count)
#22.Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
# Dictionary
my_dict = {'a': 10, 'b': 15, 'c': 7}

# Find the key with the maximum value
max_key = max(my_dict, key=my_dict.get)

# Print the result
print(f"The key with the maximum value is: {max_key}")
#23.Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
# Create a dictionary mapping numbers 1 to 5 to their squares
squares_dict = {x: x**2 for x in range(1, 6)}

# Print the dictionary
print(squares_dict)
#24.Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}.
# Alternative using a set to remove duplicate values
my_dict = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

# Using a set to track seen values and create a new dictionary with unique values
seen = set()
unique_values_dict = {k: v for k, v in my_dict.items() if v not in seen and not seen.add(v)}

print(unique_values_dict)
#25.Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def get_value_from_dict(my_dict, key):
    # Check if the key exists in the dictionary
    if key in my_dict:
        return my_dict[key]
    else:
        return "Key not found"
my_dict = {'a': 10, 'b': 20, 'c': 30}
print(get_value_from_dict(my_dict, 'b'))  # Output: 20
print(get_value_from_dict(my_dict, 'd'))  # Output: Key not found
#Challenging Problems
#26.Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.
# Given dictionaries
dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7}
result = {key: dict1[key] + dict2[key] for key in dict1 if key in dict2}

print(result)
#27.Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.
# Take user input for the value of n
n = int(input("Enter a positive integer n: "))
cube_dict = {i: i**3 for i in range(1, n+1)}
print(cube_dict)
#28.Flatten the following nested dictionary into a single-level dictionary:
#{'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
# Original nested dictionary
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
flat_dict = {}

for outer_key, inner_dict in nested_dict.items():
    for inner_key, value in inner_dict.items():
        # Combine the outer and inner keys to form a new key
        flat_dict[f"{outer_key}_{inner_key}"] = value
print(flat_dict)
#29.Write a Python program to split a dictionary into two based on whether the values are odd or even.
# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
odd_dict = {}
even_dict = {}
for key, value in my_dict.items():
    if value % 2 == 0:  
        even_dict[key] = value
    else: 
        odd_dict[key] = value

print("Odd values dictionary:", odd_dict)
print("Even values dictionary:", even_dict)
#30.Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.
# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {key: value for key, value in my_dict.items() if value >= 3}
print(filtered_dict)
#                                    The End!!!!!!!!!!!!!!!!!!!!!!!!