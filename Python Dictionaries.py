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
