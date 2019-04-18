def recbinary(seq,target,first,last):
    if first>last:
        return False
    else:
        mid=(first+last)//2
        if seq[mid]==target:
            return True
        elif seq[mid]>target:
            return recbinary(seq,target,first,mid-1)
        else:
            return recbinary(seq,target,mid+1,last)
l=[2,5,8,9,14,15,20,25]
print(recbinary(l,21,0,len(l)-1))
