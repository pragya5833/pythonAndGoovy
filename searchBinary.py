def binSearch(start,stop,li,num):
    mid=(start+stop)//2
    if li[mid]==num:
        print("Number", num, "found at", mid)
    elif num>li[mid]:
        binSearch(mid+1,len(li),li,num)
    elif num<li[mid]:
        binSearch(0,mid-1,li,num)
    else:
        print("Number not found")
li=[2,5,6,7,8,10]
binSearch(0,len(li),li,5)

    