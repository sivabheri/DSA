# Brute Force
def Method1(arr, target):
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

def Method2(arr,target):
    target = int(input())
    map = {}
    pairs = []
    seen = {}
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen[num] = True
    return pairs

def Method3(arr, target):
    arr.sort()
    pairs = []
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs

if __name__=='__main__':
    arr = [int(i) for i in input().split()]
    target = int(input())
    print(Method1(arr,target))


# New Method
def count_unique_pairs_with_sum(arr, target):
    mpp = {}
    pairs = []
    count = 0

    for num in arr:
        complement = target - num

        # Check if the complement exists in 'mpp' and its count is greater than 0
        if complement in mpp and mpp[complement] > 0:
            count += 1
            pairs.append((min(num, complement), max(num, complement)))
            mpp[complement] -= 1  # Reduce count of the complement to avoid counting the pair again
        else:
            # If 'num' already exists in the map, increment its count
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1

    return count, pairs

# Example usage
arr = [1, 59, 30, 30, 59, 1]
target = 60
cnt, unique_pairs = count_unique_pairs_with_sum(arr, target)
print(f"Count: {cnt}")  # Output: 3
print(f"Pairs: {unique_pairs}")  # Output: [(1, 59), (1, 59), (30, 30)]

# New Method 2
def find_unique_pairs_with_sum(arr, target):
    mpp = {}
    pairs = set()  # Use a set to store unique pairs

    for num in arr:
        complement = target - num

        # Check if the complement exists in 'mpp' and the pair has not been added yet
        if complement in mpp:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        
        # Add the number to the map
        if num in mpp:
            mpp[num] += 1
        else:
            mpp[num] = 1

    return pairs

# Example usage
arr = [1, 59, 30, 30, 22, 59, 20, 1, 30, 30]
target = 60
unique_pairs = find_unique_pairs_with_sum(arr, target)

# Convert the set of pairs to a list of tuples and print
print(sorted(list(unique_pairs)))  # Output: [(1, 59), (30, 30)]
