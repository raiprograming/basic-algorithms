def radixsort(seq,num):
    bins=[]
    for i in range(10):
        bins.append([])
    col=1
    for j in range(num):
        for key in seq:
            digit=(key//col)%10
            bins[digit].append(key)
        i=0
        print("after ",j,"th step",bins)
        for bin in bins:
            for k in range(len(bin)):
                seq[i]=bin[0]
                bin.remove(seq[i])
                i=i+1
                print(bin)
        i=0
        col=col*10
    return seq
h=[0,8,7,9,2,31,15,20,125]
print(radixsort(h,3))
        
            
            
        
        
        
        
            
