# Method 1
def method1():
    arr = [int(i) for i in input().split()]
    n = len(arr)
    flag = True
    for i in range(n):
        if i > 0 and arr[i-1] > arr[i]:
            flag = False
            break
    print(f"Array {arr}")
    if flag:
        print("Sorted")
    else:
        print("Not Sorted")

# Method 2 : Optimal using Binary Search - Log(N)
def method2():
    arr = [int(i) for i in input().split()]
    n = len(arr)
    print(f'Array :  {arr}')
    
    def checkSorted(arr, start, end):
        if start >= end:
            return True
        mid = (start + end) // 2
        # Check the middle element
        if (mid > start and arr[start] > arr[mid]) or (mid < end and arr[mid] > arr[end]):
            return False
        return checkSorted(arr, start, mid - 1) and checkSorted(arr, mid + 1, end)
    
    res = checkSorted(arr, 0, n - 1)

    if res:
        print("Sorted")
    else:
        print("Not Sorted")

if __name__ == "__main__":
    # Uncomment the method you want to run
    #method1()
    method2()
