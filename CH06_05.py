
total_sum = 0  # Initialize the total sum
myfile = open('numbers.txt', 'r')
# Read each line in the file
for line in myfile:
    number = int(line)
    total_sum += number  # Add the number to the total sum
print(f"{total_sum}")

