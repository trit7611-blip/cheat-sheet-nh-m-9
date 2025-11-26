largest = None
smallest = None

while True:
    value = input("Enter a number: ")

    if value == "done":
        break

    try:
        number = float(value)

        if largest is None or number > largest:
            largest = number

        if smallest is None or number < smallest:
            smallest = number

    except:
        print("Invalid input")

print("Maximum:", largest)
print("Minimum:", smallest)