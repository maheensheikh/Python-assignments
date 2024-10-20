# Assign Anton's age with type annotation
anton_age: int = 21

# Beth is 6 years older than Anton
beth_age: int = anton_age + 6

# Chen is 20 years older than Beth
chen_age: int = beth_age + 20

# Drew is as old as Chen's age plus Anton's age
drew_age: int = chen_age + anton_age

# Ethan is the same age as Chen
ethan_age: int = chen_age

# Print the names and ages
print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")

#q 2
# Given variables with type annotations
name: str = "Alice"
age: int = 30  
city: str = "New York"

# Construct the sentence using an f-string
sentence: str = f"{name} is {age} years old and lives in {city}."

# Print the output
print(sentence)

#q3
# Given string with type annotation
s: str = "hElLo WoRlD"

# Capitalize the first letter and make the rest lowercase
capitalized: str = s.capitalize()

# Convert to uppercase
uppercased: str = s.upper()

# Convert to lowercase
lowercased: str = s.lower()

# Print the outputs
print(capitalized)  
print(uppercased)   
print(lowercased)   
#q4
s: str = "the quick brown fox jumps over the lazy dog"

# Find the index of "fox"
index_fox = s.find("fox")
print(f"index of 'fox' is {index_fox}")

# Count occurrences of "the"
count_the = s.count("the")
print(f"'the' appears {count_the} times")
#q5
s: str = "I love programming in Python"

# Replace "Python" with "Java"
replaced = s.replace("Python", "Java")
print(replaced)
#q6
s: str = "apple,banana,cherry,dates"

# Split into a list
split_list = s.split(",")
print(split_list)

# Join with spaces
joined_string = " ".join(split_list)
print(joined_string)
#q7
s: str = "   Python is fun!   "

# Remove leading/trailing spaces
stripped = s.strip()
print(stripped)

# Left justify with '*'
left_justified = stripped.ljust(20, '*')
print(left_justified)

# Right justify with '*'
right_justified = stripped.rjust(20, '*')
print(right_justified)
#q8
num: int = 45

# Binary representation
binary_rep = bin(num)
print(f"Binary representation: {binary_rep}")
#q9
base: int = 3
exponent: int = 4

# Power calculation
power_result = base ** exponent
print(f"Power result: {power_result}")
#q10
value: float = 12.34567

# Round to nearest integer
rounded_int = round(value)
print(f"Rounded to nearest integer: {rounded_int}")

# Round to two decimal places
rounded_two_decimals = round(value, 2)
print(f"Rounded to two decimal places: {rounded_two_decimals}")



