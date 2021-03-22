"""
Author: Aditya Kahol
Calculator for Present value of an annuity, for a project(investment)
variable payment[1] or constant payment[2] (annuities)
"""

Invest = float(input("How much did you invest?: "))
r = float(input("What is the interest rate?: "))
flag = int(input("Payments variable[1] or constant[2]: "))

if flag == 2:
    n = float(input("How many payments will you receive?: "))
    C = float(input("How much will you receive each time?: "))
    present_value = (C/r)*(1 - (1/((1+r)**n)))
elif flag == 1:
    n = float(input("How many payment?: "))
    k = 1
    present_value = 0
    while k<=n:
        print("Payment",str(k)+"): ")
        x = float(input())
        present_value += x/((1+r)**k)
        k += 1

print()
print("The present value of this investment should be:",present_value)

if Invest < present_value:
    print("Nice!!, it's a profitable investment of:",present_value-Invest)
else:
    print("It's not a profitable investment:",present_value - Invest)
