"""
   Calculating the Hourly wage of workers
   Separately calculating the overtime wage

"""

hours = int(input("enter hours"))
rate = float(input("Enter rate "))
ot_rate = float(rate * 1.5)
ot_hours = int(hours - 40)
if hours <= 40 :
    pay = hours * rate
    print(pay)
else :
    pay = (40 * rate ) + (ot_hours * ot_rate)
    print(pay)
