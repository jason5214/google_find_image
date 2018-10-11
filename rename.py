import os


f = open('C:\\Users\Administrator\Desktop\python\DQDname.txt', 'r')
DQDrename = {}
for line in f.readlines():
    line = line.strip()
    if not len(line):
        continue
    DQDrename[line.split(' ')[0]] = line.split(' ')[1]
f.close()
print('共有',len(DQDrename),'个结果')
print(DQDrename['66'])

for k in DQDrename.keys():
    path = 'C:\\Users\Administrator\Desktop\DQD4 (1)'