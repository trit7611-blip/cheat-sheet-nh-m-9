filename = input("Enter the file name: ")
if filename == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
try:
    filehand = open(filename)
except:
    print("File cannot be opened:", filename)
    quit()
count = 0 
for line in filehand:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", filename)
