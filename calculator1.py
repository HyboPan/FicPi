#!/usr/bin/env python3
import sys
def calculate(wage):
    if wage <= 3500:
        return 0
    elif wage > 3500:
        taxincome = wage - 3500
        if taxincome <= 1500:
            tr = 0.03
            ed = 0
        elif 1500 < taxincome <= 4500:
            tr = 0.10
            ed = 105
        elif 4500 < taxincome <= 9000:
            tr = 0.20
            ed = 555
        elif 9000 < taxincome <= 35000:
            tr = 0.25
            ed = 1005
        elif 35000 < taxincome <= 55000:
            tr = 0.30
            ed = 2755
        elif 55000 < taxincome <= 80000:
            tr = 0.35
            ed = 5505
        elif 80000 < taxincome:
            tr = 0.45
            ed = 13505
        return taxincome * tr -ed
if __name__ == "__main__":
    try:
        num = len(sys.argv)
        num == 2
        wage = int(sys.argv[1])
    except Exception:
        print("Parameter Error")
    print(format(calculate(wage), ".2f"))
