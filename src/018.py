s='ATGTTATAG'
s_dic={'A':'T','G':'C','C':'G','T':'A'}
s=('.').join(s)
s=s.split('.')
for i in range(len(s)):
    s[i]=s_dic[s[i]]

print(('').join(s))
    
    
