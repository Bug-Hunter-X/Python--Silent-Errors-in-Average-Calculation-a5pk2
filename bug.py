def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers) 
    return average

# Example usage (may cause ZeroDivisionError):
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 0 as expected

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 20.0 as expected

my_numbers = [10, 20, 0, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 15.0 as expected

#Example of silent error
my_numbers = [10, 20, 'a', 30] #This will cause a TypeError
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will raise a TypeError because of the string 'a'