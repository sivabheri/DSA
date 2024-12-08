from collections import Counter
from functools import cmp_to_key

def count_sort(a, b, freq):
    if freq[a] != freq[b]:
        return freq[b] - freq[a]  # Sort by frequency (higher comes first)
    return a - b  # Sort by value (smaller comes first if frequency is the same)

class Solution:
    def freqSort(self, arr):
        freq = Counter(arr)
        
        # Using cmp_to_key to use count_sort as a comparison function
        arr.sort(key=cmp_to_key(lambda a, b: count_sort(a, b, freq)))

        return arr

if __name__ == "__main__":
    solution = Solution()
    arr = [3, 3, 2, 1, 2, 3]
    sorted_arr = solution.freqSort(arr)

    print(" ".join(map(str, sorted_arr)))
