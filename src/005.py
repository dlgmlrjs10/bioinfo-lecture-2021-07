#! /usr/bin/enb python 

num1=input('number : ')

num1=int(num1)

if num1%3==0 and num1%7==0:
    print('number는 3과 7의 배수')
elif num1%3==0 and num1%7!=0:
    print('number는 3의 배수')
elif num1%7==0 and num1%3!=0:
    print('number는 7의 배수')
else:
    print('아무것도 아님')


##강사님

#sys.argv사용, default의 result를 3과 7의 배수 모두 아님. 으로 놓고 if elif를 사용하여 result값을 바꿔주도록 함
