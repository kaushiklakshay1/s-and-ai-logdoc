import sys
from collections import Counter
filename = sys.argv[1]
with open (filename) as f:
    lines = f.readlines()

print("Total lines:",len(lines))

counts = Counter()
for line in lines:
    feilds = line.split()

    if len(feilds) >= 4:
        key = feilds[3]
        count[key]+=1

print("TOP 5:")
for item, n in counts.most_common(5):
    print(item,n) 
