def read_data(file):
    
    f = open(file,'r')
    toReturn = {}
    f1 = open("1n.txt",'w')
    digits = "0123456789"
    for i in f:
        ctr = 0
        while(i[ctr] in digits):
            ctr = ctr +1
        f1.write(i[ctr:])
        f1.flush()
    
read_data("1.txt")
