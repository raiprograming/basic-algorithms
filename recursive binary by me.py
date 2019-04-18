def recbinary(seq,target,first,last):
    if first>=last:
        return False
    mid=(first+last)//2
    if seq[mid]==target:
        return True
    else:
        if seq[mid]>target:
            return recbinary(seq,target,first,mid-1)
        else:
            return recbinary(seq,target,mid+1,last)
l=[2,5,6,8,10,15,20,25]
print(recbinary(l,21,0,len(l)-1))
