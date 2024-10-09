with open('names.txt', 'r') as myfile:
    # Initialize a counter for the names
    count = 0        
    # Read each line and increment the counter
    for line in myfile:
        count += 1  # Each line represents a name
# Display the number of names
print(f'{count}')
