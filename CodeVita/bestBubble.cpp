BestBubble
Problem Description
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. The problem with bubble sort is its worst case scenario. When the smallest element is in the last position, then it takes more time to sort in ascending order, but takes less time to sort in descending order.

An array is called beautiful if all the elements of the array are in either ascending or descending order. Given an array of numbers, find the minimum swap operations required to make the array beautiful.

Constraints
0 < N < 1000

0 < Arr[i] < 1000

Input
First line contains of integer N denoting number of elements in the array.

Second line consist of N integers separated by space denoting the elements of the array.

Output
Single integer denoting the least numbers of swap operations required to make the array beautiful.

Time Limit (secs)
1

Examples
Example 1:

Input:

5

4 5 3 2 1

Output:

1

Explanation:

The number of swaps required to sort the elements in ascending order is 9.

The number of swaps required to sort the elements in descending order is 1.

The best way is to sort in descending order and swaps required is 1.

Example 2:

Input:

5

4 5 1 2 3

Output 2:

4

code:

#include<bits/stdc++.h>
using namespace std;
int sortSwaps(vector<int>& arr,bool dirn) {
  int n = arr.size();
  int cnt=0;
  for (int i=1;i<n;++i) {
    int ind=arr[i];
    int j=i-1;
    while (j>=0 && ((dirn && arr[j]>ind) || (!dirn && arr[j]<ind))) {
      arr[j+1]=arr[j];
      --j;
      ++cnt;
    }
    arr[j + 1] = ind;
  }
  return cnt;
}
int minSwaps(const vector<int>& arr) {
  vector<int> ascArr = arr;
  vector<int> desArr = arr;
  int ascSwaps = sortSwaps(ascArr,true);
  int descSwaps = sortSwaps(desArr,false);
  return min(ascSwaps,descSwaps);
}
int main() {
  int n;
  cin >> n;
  vector<int> arr(n);
  for (int i=0;i<n;++i) {
    cin >> arr[i];
  }
  cout << minSwaps(arr) << endl;
  return 0;
}