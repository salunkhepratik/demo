total_sum = 0

# Loop to take input for 10 numbers
for i in range(1, 11):
    # Get input from the user
    number = float(input(f"Enter number {i}: "))
    
    # Add the number to the total sum
    total_sum += number

# Display the total sum
print(f"The total sum of the 10 numbers is: {total_sum}")
