print("enter common series")
c="19F61A06"
print("end series ony single digit ony in caps")
e=input()
i='N'
l=[]
if(e<='9'):
    print("eve")
    for i in range(0,100):
        if(i<10):
            a=c+'0'+str(i)
            print(a)
        else:
            a=c+str(i)
            print(a)
"""else:
    for i in range(1,99)"""
