#! /usr/bin/env python
import sys
number=int(sys.argv[1])
result=1
while number !=0:
    result*=number
    number-=1

print(result)
    
