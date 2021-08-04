def sorting(li):
    for i in range(0,len(li)):
        for j in range(0,len(li)):
            if j+1<len(li) and li[j]>li[j+1]:
                temp=li[j]
                li[j]=li[j+1]
                li[j+1]=temp
            else:
                continue
    print(li)
sorting([3,5,1,2])
