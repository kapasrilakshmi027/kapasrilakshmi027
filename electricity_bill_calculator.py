# Electricity Bill Calculator using Functions

def get_units():
    return int(input("Enter total units consumed: "))


def calculate_bill(units):
    if units<=100:
        bill = units*1.5
    elif units<=200:
        bill=(100*1.5)+((units-100)*2.5)
    elif units<= 300:
        bill=(100*1.5)+(100*2.5)+((units-200)*4)
    else:
        bill=(100*1.5)+(100*2.5)+(100*4)+((units-300)*6)

    return bill


def display_bill(units, bill):
    print("\n----- ELECTRICITY BILL -----")
    print("Units Consumed:", units)
    print(f"Total Amount: ₹{bill:.2f}")


def main():
    units = get_units()
    bill = calculate_bill(units)
    display_bill(units, bill)


main()
