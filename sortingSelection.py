def selectSort(li):
    for i in range(0,len(li)):
        mini=i
        for j in range(i,len(li)):
            if li[mini]>li[j]:
                mini=j
            else:
                continue
        temp=li[i]
        li[i]=li[mini]
        li[mini]=temp
    print("sorted list is: ", li)
selectSort([2,10,0,11])