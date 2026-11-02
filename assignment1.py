
# Que 1: String Concatenation

string1 = "Hello "
string2 = input("Enter your Name: ")

# Concatenate the two strings
result = string1 + string2

print(result)

# Add the welcome message
string3 = ", welcome to Python programming"
result = result + string3

print(result)



# Que 2: String Slicing and Indexing

print("First character:", result[0])

print("Last character:", result[-1])

print("First 5 characters:", result[:5])

print("Last 11 characters:", result[-11:])

print("Reverse string:", result[::-1])

print("Word Python:", result[22:29])

# Que 3: String Methods

strM = "Python beginner tutorial"

# a. Convert the sentence to uppercase
print("Uppercase:", strM.upper())

# b. Convert the sentence to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize the sentence
print("Capitalized:", strM.capitalize())

# d. Count the occurrences of character 't'
print("Count of t:", strM.count('t'))

# e. Replace Python with Machine Learning
print("Replaced:", strM.replace("Python", "Machine Learning"))


# Question 4: Tuples

# Create two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# b. Repeat the elements 3 times
print("Repeated tuple:", t_combine * 3)

# c. Access the 3rd element
print("3rd element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])
