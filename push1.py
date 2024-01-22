def push(arr,stack,top):
    if(top==stack):
        print("\n stack overflow ")
    else:

        k=int(input())
        arr.append(k)
        top=top+1
        print(arr[top],"is the new top in the stack")
        print("\n",arr)
    return arr,top
top=0
stack = 10
arr=[1,5,8,9,6,12]
size=len(arr)
top=size-1
arr,top=push(arr,stack,top)
#print(stack,top,size,arr)
arr,top=push(arr,stack,top)
arr,top=push(arr,stack,top)
arr,top=push(arr,stack,top)
arr,top=push(arr,stack,top)
arr,top=push(arr,stack,top)
arr,top=push(arr,stack,top)
arr,top=push(arr,stack,top)