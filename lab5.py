import sys

def simple_interest(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = int(input("Enter principal amount:"))
    i = float((input("Enter interest rate:"))
    t = int(input("Enter time in years:"))

    print("Simple interest is:", simple_interest(p, i, t))
