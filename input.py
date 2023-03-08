inp = [x.strip().split(':') for x in input().strip().split(';')]
resinp=[]
for x in inp:
    tx=[]
    for y in x:
        tx.append(y.strip().split(' - '))
    resinp.append(tx)
for i in range(len(resinp)):
    resinp[i][0][0]=(resinp[i][0][0][(resinp[i][0][0].find('$')+1):]).strip()
print(resinp)