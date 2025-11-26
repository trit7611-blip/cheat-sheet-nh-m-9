numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input")

if numbers:
    maximum = max(numbers)
    minimum = min(numbers)
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
else:
    print("No numbers entered.")
    