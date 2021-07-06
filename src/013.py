import sys
try:
    num=int(input('Enter:'))
    print(10/num)
except ZeroDivisionErrorr:
    print('division 0')
    sys.exit()
except ValueError:
    print('value  error')
    sys.exit()

