num = int (input("enter a num"))
zicaron = int (input("enter a zicaron"))
def BinNegative(num,zicaron):
    BinNum=bin(num)[2:]
    temp = int(BinNum)
    i=0#מספר הסיביות שצריך להוסיף
    while temp >0:
        i=i+1
        temp=temp//10
    StrBin= (zicaron-i)*"0" +str(bin(num)[2:])
    print(" Positive "+StrBin)
    StrBin=StrBin.replace("0","2")
    StrBin=StrBin.replace("1","0") 
    StrBin=StrBin.replace("2","1")
    counter = len(StrBin)-1
    print(" complementary to one "+StrBin)
    if (StrBin[len(StrBin)-1])=="0":
        StrBin =StrBin[0:len(StrBin)-1]
        StrBin= StrBin +"1"
    else:
        while StrBin[counter]!="0":
            counter = counter-1
        StrBin =StrBin[0:counter]
        StrBin= StrBin +"1"+((zicaron - counter)-1)*"0"
    print(" Negative "+StrBin)
BinNegative(num,zicaron)
     
    
