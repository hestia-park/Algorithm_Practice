import collections
T=3
t1=[[6,6,7,7,6,7],[0,5,4,0,6,0],[1,0,1,1,2,3]]

for i in t1:
    counters=collections.Counter(i)
    print(counters)
    ans=False
    for j in counters:
        if counters[j]>=3:
            ans=True
            counters[j] -= 3

    print(ans)