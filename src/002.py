#! /usr/bin/env python

r=input('원의 반지름: ')
while not r.isdigit():
    r=input('다시 원의 반지름: ')
r=float(r)

print(r**2*3.14)
