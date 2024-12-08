
# Find the longest common prefix in string 1 which is common in string 2

def longesCP(s1 , s2) :

	n = len(s1)

	for i in range(n) :

		prefix = s1[:i+1]

		if prefix in s2:

			max_length = i+1

		else:
			break

	if max_length == 0 :
		return (-1,-1)

	return (0,max_length)

if __name__ == '__main__':
	
	s1 = "practiceCoding"
	s2 = "preppractice"

	print(longesCP(s1,s2))