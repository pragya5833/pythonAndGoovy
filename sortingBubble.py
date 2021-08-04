def bubSort(li):
    for i in range (0,len(li)):
        for j in range(0,len(li)):
            if j+1<len(li) and li[j+1]<li[j]:
                temp=li[j]
                li[j]=li[j+1]
                li[j+1]=temp
    print("Sorted list is: ",li)
bubSort([10,6,8,3])