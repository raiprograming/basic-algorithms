def quicksort(seq):
    n=len(seq)
    recquicksort(seq,0,n-1)
    return seq
def recquicksort(seq,first,last):
    if first>=last:
        return
    else:
        pivot=seq[first]
        pos=partition(seq,first,last)
        recquicksort(seq,first,pos-1)
        recquicksort(seq,pos+1,last)
def partition(seq,first,last):
    pivot=seq[first]
    left=first+1
    right=last
    while left<=right:
        while left<right and seq[left]<pivot:
            left=left+1
        while right>=left and seq[right]>=pivot:
            right-=1
        if left<right:
            seq[left],seq[right]=seq[right],seq[left]
    if right!=first:
        seq[first]=seq[right]
        seq[right]=pivot
    return right
            
