filename = input("Enter the name of the file: ")
with open(filename, 'r') as file:
    Counter = 1
    for line in file:
        if line: 
             print(f'{counter}:{line}')
             Counter =+ 1