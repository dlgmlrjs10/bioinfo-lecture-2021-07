file_name='covid19.fasta.gz'
import gzip 
data=dict()
with gzip.open(file_name,'rt') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        for base in line.strip():
            if base not in data:
                data[base]=0
            data[base]+=1

print(data)
