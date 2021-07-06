try:
    with open('noname.txt','r') as fr:
        read=fr.readlines()
except FileNotFoundError as err:
    print(f'error is {err}')
    

