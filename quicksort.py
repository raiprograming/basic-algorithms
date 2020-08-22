'''def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while(i<j):
        while(i<j and arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp'''
'''def partition(arr,low,high): 
    i = ( low-1 )
    print(i)
    # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )'''
def partition(arr,beg,end):
    left=beg
    right=end
    lock=beg
    
    while(left<right):
        while(arr[lock]<=arr[right] and right!=lock):
            right -=1
        if lock==right:
            return lock
        if(arr[lock]>arr[right]):
            temp=arr[lock]
            arr[lock]=arr[right]
            arr[right]=temp
            lock=right
        while(arr[lock]>=arr[left] and left!=lock):
            left +=1
        if lock==left:
            return lock
        if(arr[lock]<arr[left]):
            temp=arr[lock]
            arr[lock]=arr[left]
            arr[left]=temp
            lock=left
    return lock
    
l=[10,7,8,9,1,5]
print(l)
a=partition(l,0,5)
print(a)
print(l)
def quicksort(arr,low,high):
    if low<high:
        print(arr)
        pi=partition(arr,low,high)
        print(pi)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
quicksort(l,0,5)
print(l)


            
        


