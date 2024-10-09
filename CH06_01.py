myfile = open('numbers.txt', 'r')
# Read each line in the file
for line in myfile:
# Convert the line to an integer and print it
    number = int(line)
    print(number)

# Close file
myfile.close

