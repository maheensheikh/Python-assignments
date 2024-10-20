

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def explore_favorite_numbers() -> None:
    """Interactive tool to explore favorite numbers."""
    # Get user's name
    name: str = input("Enter your name: ")
    
    # Get three favorite numbers and store them in a list
    favorite_numbers: list[int] = []
    for i in range(1, 4):
        number: int = int(input(f"Enter your {['first', 'second', 'third'][i-1]} favorite number: "))
        favorite_numbers.append(number)
    
    # Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    
    # Check if numbers are even or odd and store in a list of tuples
    even_odd_info: list[tuple[int, str]] = []
    for number in favorite_numbers:
        even_odd_info.append((number, "even" if number % 2 == 0 else "odd"))
    
    # Display if the numbers are even or odd
    for number, status in even_odd_info:
        print(f"The number {number} is {status}.")
    
    # Iterate over numbers and print their square
    print("\nHere are your numbers and their squares:")
    for number in favorite_numbers:
        square_tuple: tuple[int, int] = (number, number ** 2)
        print(f"The number {number} and its square: {square_tuple}")
    
    # Calculate the sum of the numbers
    total_sum: int = sum(favorite_numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still a cool number!")

# Run the program
explore_favorite_numbers()
