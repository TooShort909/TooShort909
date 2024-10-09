filename = input("Enter the name of the file: ")
with open(filename, 'r') as file:
# Read the first five lines
    lines = [file.readline() for _ in range(5)]
    # If there are fewer than 5 lines
    if len(lines) < 5:
            for line in file:
                print(line)
    for line in lines:
        if line:  
            print(line)

    
               