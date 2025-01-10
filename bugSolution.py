def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: 0

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: 20.0

my_numbers = [10, 20, 0, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: 15.0

#This will now raise a TypeError
try:
    my_numbers = [10, 20, 'a', 30] 
    result = calculate_average(my_numbers) 
    print(f"The average is: {result}")
except TypeError as e:
    print(f"Error: {e}") #Prints: Error: List must contain only numbers.