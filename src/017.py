s='ATGTTATAG'
for i in range(1,(len(s)//3)+1):
    print(s[(i*3-3):i*3])

print(s[::-1])
