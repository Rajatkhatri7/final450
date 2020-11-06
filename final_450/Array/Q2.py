def MinMax(low,high,arr):

    # as python has min() and max() methods already we can directly use them but 
    # for logic building we harcode another method

    '''
    Divide the array into two parts(like merge sort) and 
    compare the maximums and minimums of the two parts
    to get the maximum and the minimum of the whole array.

    '''

    minele = arr[low] #initially let both at same position
    maxele = arr[low]

    if low==high:# when 1 element in the array
        minele = arr[low]
        maxele = arr[low]

        return (minele,maxele)

    elif high == low+1: # when 2 elements in arr

        if arr[high]>arr[low]:
            maxele = arr[high]
            minele = arr[low]

        else:
            maxele = arr[low]
            minele = arr[high]
        return (minele,maxele)
    


    else:
        # when more then 2 element in the array
        mid = int((low+high)/2)
        minele_1,maxele_1 = MinMax(low,mid,arr)
        minele_2,maxele_2 = MinMax(mid+1,high,arr)

    return ( min(minele_1,minele_2), max(maxele_1,maxele_2))



arr = [int(_) for _ in input("enter elements: ").split()]

low=0
high = len(arr)-1
mi,mx = MinMax(low,high,arr)
print(mi)
print(mx)        
        



