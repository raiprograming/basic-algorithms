def move(n,src,dest,temp):
    if n>=1:
        move(n-1,src,temp,dest)
        print("moving ",src,"to",dest)
        move(n-1,temp,dest,src)
move(3,"A","C","B")
