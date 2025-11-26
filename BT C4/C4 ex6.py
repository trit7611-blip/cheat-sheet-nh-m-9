def computepay(hours, rate):
    standard_hours = 40

    if hours <= standard_hours:
        pay = hours * rate
    else:
        regular_pay = standard_hours * rate
        overtime_hours = hours - standard_hours
        overtime_rate = rate * 1.5
        overtime_pay = overtime_hours * overtime_rate
        pay = regular_pay + overtime_pay
        
    return pay

try:
    s_hours = input("Enter Hours: ")
    f_hours = float(s_hours)
    
    s_rate = input("Enter Rate: ")
    f_rate = float(s_rate)
    print("Enter Hours: ",s_hours)
    print("Enter Rate: ",s_rate)
    pay = computepay(f_hours, f_rate)
    print("Pay: ",pay)

except:
    print("Error, please enter numeric input for hours and rate.")