def fileCheck():
    f1=open("first.txt",'w')
    l=["i see\n","this is\n","written as\n","list\n","with writelines\n"]
    m=["i see\n","i am to\n","test\n","lines\n"]
    f1.writelines(l)
    f1.close
    f2=open("second.txt",'w')
    f2.writelines(m)
    f2.close()
fileCheck()
def filread():
    f1=open("first.txt","r")
    f2=open("second.txt","r")
    content_listOne=f1.readlines()
    content_listTwo=f2.readlines()
    length_listOne=len(f1.readlines())
    length_listTwo=len(f2.readlines())
    print(content_listOne)
    count={}
    # if length_listOne>length_listTwo:
    for eachTwo in content_listTwo:
        print("in first loop",eachTwo)
        for eachOne in content_listOne:
            print("in second loop",eachOne)
            if eachOne == eachTwo:
                if eachOne in count.keys():
                    count[eachOne]=count[eachOne]+1
                else:
                    count[eachOne]=1
    print(count)
filread()

