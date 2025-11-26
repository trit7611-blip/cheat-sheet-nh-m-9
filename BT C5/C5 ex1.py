total = 0
count = 0

while True:
    value = input("Enter a number: ")

    if value == "done":
        break

    try:
        number = float(value)
        total += number
        count += 1
    except:
        print("Invalid input")

if count > 0:
    print(total, count, total / count)
else:
    print("No numbers were entered.")