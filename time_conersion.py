#convert time in 12hr format
#time=21:59:60
#10:00:00
time='00:59:60'
l1=time.split(':')
l1.append('pm' if int(l1[0])>12 else 'am')
l1[0]=int(l1[0])-12 if int(l1[0])>=12 else l1[0]
if int(l1[2])==60:
    l1[2]='00'
    l1[1]=int(l1[1])+1
if int(l1[1])==60:
    l1[1]='00'
    l1[0]=int(l1[0])+1
if int(l1[0])==13:
    l1[0]='01'
print(str(l1[0])+':'+str(l1[1])+':'+str(l1[2])+' '+l1[3])