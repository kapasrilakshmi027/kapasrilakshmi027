#user input INR amount 
inr_amount=float(input("Enter amount in INR: "))
# USD rate
usd_rate = 0.012
#currency conversion
usd_amount=inr_amount*usd_rate
#conversion result
print("\n-----currency coversion-----")
print("Amount in INR:",inr_amount)
print("Converted to USD:",usd_rate)

