a_list=[3,1,1,2,0,0,3,3,3]
a_dict={}
for i in range(len(a_list)):
    if a_list[i] not in a_dict:
        a_dict[a_list[i]]=0
    a_dict[a_list[i]]+=1
print(a_dict)
