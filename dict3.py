#keys are ages of voters and values are votes
cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
    }
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
    }
countc,countb=0,0
for k,v in cong.items():
    if k>=18:
        countc+=v
for k,v in bjp.items():
    if k>=18:
        countb+=v
print("bjp"  if countb>countc else "cong","won by",abs(countb-countc),"votes")