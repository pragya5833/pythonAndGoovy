def separation(value):
    l1=[]
    l2=[]
    #"https://meet.google.com/rsm-nxjt-xen?authuser=1"

    for i in value:
        print(i)
        if i=='"':
            l1.append(i)
        else:
            l2.append(i)
    print(l1)
separation("https://meet.google.com/rsm-nxjt-xen?authuser=1")
