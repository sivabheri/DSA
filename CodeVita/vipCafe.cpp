Vipcafe:
Problem Description
Raj is running the busiest cafe in the city. It is also the most visited cafe by VIPs.

VIPs buys costly Beverages. It gives Raj's Cafe high profit. Raj asked his workers to prefer serving VIPs first, because VIPs don't like to wait much time. Whenever a person orders something, Raj gives priority values to the orders and adds it to the queue. The greater the value more important the order is.

The workers start to serve the orders with high priority in queue ensuring that the VIPs get theirs orders quickly. However, those orders having low priority have to wait for a long time in queue,upsetting those people. This reduces the total number of people visiting the cafe and reducing the profit. But, making first come first serve basis reduces the VIPs visiting the cafe. This also reduces the profit.

Raj came up with a new idea to keep the profit high. He introduced a new concept called dynamic priority. The priority of orders changes while in the queue. Raj will maintain a queue of orders with assigned priority,adding new orders at end. The order with high priority in the queue will be served first .When an order got served due to its high priority, the priority of orders in the queue before this will be increased by one. If two orders having same priority ,then the order which was en-queued first will be served first. This strikes a balance between reducing the waiting time of VIPs and also serving other people without much delay.

One day, his friend visited the cafe and ordered something. As usual his order got some priority and got added in the queue. After some time his friend lost his patience and asked when will his order be served. After that, Raj stopped adding new orders to the queue and started calculating after how many orders his friend will get served, considering only orders currently in the queue. Given the queue, can you find after how many orders will Raj's friend get served?

Constraints
2 <= N <= 25

1 <= Priority <= 100

1 <= K <= N

Input
First line contains a Integer 'N' denoting the total orders in cafe which are needed to served.

Second line consist 'N' space separated Integers indicating the priority of orders present in the queue.

Third line consist of integer 'K' indicating the position of his friend in the queue.

Output
Single Integer denoting after how many orders will Raj's friend get served.

Time Limit (secs)
1

Examples
Input

6

1 3 5 2 4 6

4

Output

6

Explanation

There are 6 orders in the queue with priorities 1 3 5 2 4 6 and Raj's friend's order is at the 4th place. Thus, Raj's friend's order priority is 2. The serving will be as illustrated below:

1 3 5 2 4 6

2 4 6 3 5 x

3 5 x 3 5 x

4 x x 3 5 x

5 x x 4 x x

x x x 4 x x

The order 6th will be served first because 6 is the maximum. The priority of orders before it will be incremented by 1. Next order be 3rd , 2nd and so on. His friend's order will be served last i.e. 6th.

Example 2

Input

5

1 4 3 2 5

3

Output

3

Explanation

There are 5 orders in the queue with priorities 1 4 3 2 5 and his friend's order is at the 3rd place. Raj's friend's order priority is 3. The serving will be as illustrated below:

1 4 3 2 5

2 5 4 3 x

3 x 4 3 x

4 x x 3 x

The order 5th will be served first because 5 is the maximum. The priority of orders before it will be incremented by 1. Next order served will be the 2nd one in the queue. His friend's order will be served 3rd.

sol:

'''
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int>& arry, int position) {
  int index = -1, maxVal = -1;
  int n = arry.size();
  for (int i = 0; i < n; i++) {
    if (arry[i] > maxVal) {
      maxVal = arry[i];
      index = i;
    }
  }
  if (index == position) return 0;
  arry[index] = -1;
  for (int i = 0; i < index; i++) {
    if (arry[i] > 0) {
      arry[i]++;
    }
  }
  return 1+solution(arry,position);
}

int main() {
  int n;
  cin >> n;
  vector<int> arry(n);
  for (int i = 0; i < n; i++) {
    cin >> arry[i];
  }
  int k;
  cin >> k;
  k--;
  cout << 1+solution(arry,k) << endl;
  return 0;
}

'''