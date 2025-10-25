'''
Given a sorted array of integer arr and an integer target
Find the index of the first and last position of target in arr

If target cannot be found in arr, return [-1,-1]
'''

def first_and_last(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            start = i
            while i+1 < len(arr): #and arr[i+1] == target:
                i+=1
            return [start, i]
    return [-1,-1]


def main():
    arr = [5,0,1,2,3,4,4,6,6,6,6,7,8,9,10,5]
    target = 5
    
    print(first_and_last(arr,target))

if __name__ == "__main__":
    main()