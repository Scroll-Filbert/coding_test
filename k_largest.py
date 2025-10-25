def kth_largest(arr, k):
    '''manual

    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

    '''
    
    arr.sort()
    n = len(arr)
    return arr[n-k]
    

def main():
    arr = [0,1,2,4,5,6,8,9,4,2,5,7,8,5]
    k = 4

    print(kth_largest(arr,k))

if __name__ == "__main__":
    main()