list1=[1,5,3,2,-1,4,31]
n= len(list1)
for i in range(0,n):
    for j in range(i+1, n):
        if list1[i]>=list1[j]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
print(list1)