def mergesort(seq):
    if len(seq)>1:
        mid=len(seq)//2
        l=seq[:mid]
        r=seq[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                seq[k]=l[i]
                i=i+1
            else:
                seq[k]=r[j]
                j=j+1
            k=k+1
        while i<len(l):
            seq[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            seq[k]=r[j]
            j=j+1
            k=k+1
print("welcome to the mergesort program")
n=int(input("enter no of elements in your array"))
arr=[]
for i in range(n):
    arr.append(int(input("enter %dth element"%i)))
print("your entered array=",arr)
mergesort(arr)
print("your array after applying mergesort algorithm",arr)
    
