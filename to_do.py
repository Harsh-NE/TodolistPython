import sys
filename="to_do_list.txt"
x=sys.argv
if(len(x)==1):
    file1=open(filename,'r')
    print("*******************************************")
    print("Here's your to-do list:")
    n=1
    for i in file1.readlines():
        print(n,".",i)
        n+=1
    print("*******************************************")
    file1.close()
    sys.exit()
elif(len(x)!=1):
    if(x[1]=="add"):
        file=open(filename,'a')
        i=2
        while(i<len(x)):
                file.write(x[i]+' ')
                i+=1
        file.write('\n')
        file.close()
        file1=open(filename,'r')
        print("*******************************************")
        print("Here's your to-do list:")
        n=1
        for i in file1.readlines():
            print(n,".",i)
            n+=1
        print("*******************************************")
        file1.close()
    elif(x[1]=="remove"):
            try:
                y=int(x[2])-1
                file=open(filename,'r')
                l1=file.readlines()
                print(l1)
                l1.remove(l1[y])
                print(l1)
                file.close()
                file1=open(filename,'w')
                file1.writelines(l1)
                file1.close()
            except:
                print("wrong")
            
sys.exit()