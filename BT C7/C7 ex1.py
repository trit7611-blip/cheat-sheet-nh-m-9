filename = input("Enter a file name: ")
file = open(filename)
for line in file:
    print(line.upper().strip())
file.close()