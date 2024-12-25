# Problem Statement
''' 
A. Buttons

Anna and Katie ended up in a secret laboratory.

There are a+b+c buttons in the laboratory. 
It turned out that a buttons can only be pressed by Anna, 
b buttons can only be pressed by Katie, 
and c buttons can be pressed by either of them. 
Anna and Katie decided to play a game, taking turns pressing these buttons. 
Anna makes the first turn. Each button can be pressed at most once, so at some point, one of the girls will not be able to make her turn.

The girl who cannot press a button loses. Determine who will win if both girls play optimally.

Input
The first line contains a single integer t
 (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of three integers a , b , and c
 (1 ≤ a, b, c ≤ 10^9 ) — the number of buttons that can only be pressed by Anna, the number of buttons that can only be pressed by Katie, and the number of buttons that can be pressed by either of them, respectively.

Output
For each test case, output First if Anna wins, or Second if Katie wins.


Example input:
5
1 1 1
9 3 3
1 2 3
6 6 9
2 2 8

output:
First
First
Second
First
Second
'''
class Test:

	def solve1(self): # TLE

		a, b, c = map(int,input().split())

		while(True):

			if c>0 :
				c-=1
			elif a>0:
				a-=1
			else:
				print("Second Wins")
				break

			if c>0 :	
				c-=1
			elif b>0:
				b-=1
			else:
				print("First Wins")
				break
			
	def solve2(self): # Accepted

		a, b, c = map(int,input().split())

		if c%2==0:

			if a>b :
				print("First")
			else:
				print("Second")
		else:
			if a>=b :
				print("First")
			else:
				print("Second")

if __name__ == '__main__':
	
	t = int(input()) # no of testcases
	obj = Test()
	for i  in range(t):

		obj.solve2()