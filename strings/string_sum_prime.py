# Audintel question 
import math
from collections import defaultdict

def isprime(num):

	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0:
			return False
	return True

def sum_of_digits(num):
    
    if num < 10:
        return num
    
    digit_sum = sum(int(digit) for digit in str(num))
    return sum_of_digits(digit_sum)

def main():

	s = input()

	prime_dict = defaultdict(int)

	i,j = 1000,0

	while(i<1182):
		while (j<26):
			if isprime(i):
				prime_dict[chr(ord('A')+j)] = i
				j+=1
			i+=1

	print(prime_dict)

	csum = 0
	for i in s:
		csum += prime_dict[i]

	print(f'Current prime sum of {s} : {csum}')
	ans = sum_of_digits(csum)

	print(f'The String with Prime Sum is :{ans}')

if __name__ == '__main__':
	main()