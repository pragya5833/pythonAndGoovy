def insertSort(li):
    for i in range(0,len(li)):
        for j in range(i,0,-1):
            if j-1>=0 and li[j-1]>li[j]:
                temp=li[j-1]
                li[j-1]=li[j]
                li[j]=temp
    print(li)
insertSort([2,10,0,11])
