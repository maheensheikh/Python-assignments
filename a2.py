#q1
# Add Two Numbers
def add_two_numbers() -> None:
    first_number: int = int(input("Enter the first number: "))
    second_number: int = int(input("Enter the second number: "))

    total_sum: int = first_number + second_number
    print(f"The sum of {first_number} and {second_number} is {total_sum}.")
#q2
# Agreement Bot
def agreement_bot() -> None:
    favorite_animal: str = input("What's your favorite animal? ")
    print(f"My favorite animal is also {favorite_animal}!")
#q3
# Fahrenheit to Celsius
def fahrenheit_to_celsius() -> None:
    fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
    
    celsius: float = (fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C")
#q4
# Triangle Perimeter
def triangle_perimeter() -> None:
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    perimeter: float = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}")
#q5
# Square of a Number
def square_of_number() -> None:
    number: float = float(input("Type a number to see its square: "))

    square: float = number * number
    print(f"{number} squared is {square}")
#q6
# Delete a number from list
def delete_number_from_list() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]
    numbers.remove(3)
    print(numbers)  # Output: [1, 2, 4, 5]

#q7
# Add elements of list2 to list1
def add_lists() -> None:
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]

    list1.extend(list2)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6]

#q8
# Pop Method
def pop_from_list() -> None:
    items: list[int] = [10, 20, 30, 40]
    removed_value: int = items.pop()  # Removes the last element (40)
    print(items)  # Output: [10, 20, 30]
    print(f"Removed value: {removed_value}")  # Output: 40

#q9
# Index Method
def index_method() -> None:
    colors: list[str] = ['red', 'blue', 'green', 'yellow']
    index_of_green: int = colors.index('green')
    print(f"The index of 'green' is {index_of_green}.")  # Output: 2

#q10
# Get Last Element from a List
def get_last_element(lst: list[int]) -> None:
    print(lst[-1])

# Example usage:
get_last_element([1, 2, 3, 4])  # Output: 4

#q11
# Get a List from User Input
def get_user_list() -> None:
    user_list: list[str] = []

    while True:
        value: str = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)

    print(f"Here's the list: {user_list}")
