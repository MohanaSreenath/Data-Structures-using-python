class Mohan:
    def bubble_sort(self,arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if(arr[i]<arr[j]):
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
        
        
agent=Mohan()
arr = [64, 25, 12, 22, 11]
agent.bubble_sort(arr)
for arr in arr:
    print(arr)
