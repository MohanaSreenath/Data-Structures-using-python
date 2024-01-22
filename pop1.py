def pop(arr,top):
    if(top==0):
        print("\n stack underflow ")
    else:
        arr[top]=None
        top=top-1
        print(arr[top],"is the new top in the stack")
    return arr,top

top=0
arr=[1,5,8,9,6,12]
size=len(arr)
top=size-1
arr,top=pop(arr,top)
#print(top,size,arr[top])
arr,top=pop(arr,top)
arr,top=pop(arr,top)
arr,top=pop(arr,top)
arr,top=pop(arr,top)
arr,top=pop(arr,top)