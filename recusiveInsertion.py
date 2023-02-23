 
def insertion_sort(A,index):
    
    if index==0:
        return

    insertion_sort(A,index-1)
    key=A[index]
    i=index-1
    while i>=0 and key < A[i]:        
        A[i+1]=A[i]
        i=i-1
    print('index:   ',index)
    print('key  ',key)
    A[i+1] = key
    print(A)
    

    


if (__name__=="__main__"):
    A=[5,4,3,2,1,0,-1,-2,-3,-4]
    insertion_sort(A,len(A)-1)
    print(A)

