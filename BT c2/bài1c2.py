Hours = float(input("Enter hours: "))
Rate = float(input("Enter rate: "))
if Hours > 40:
    Pay = 40 * Rate + (Hours - 40) * Rate * 1.5
else:
    Pay = Hours * Rate
print("Pay:", Pay)

