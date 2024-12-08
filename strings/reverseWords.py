
# Program to reverse the words in a string 
# input = 'The sky is Blue'
# output = 'Blue is sky The'

# Method 1 : Using Lists, reversed function and join


def method1(s):

	store1 = [i for i in s.split()]

	temp = list(reversed(store1))

	return ' '.join(i for i in temp)   # TC : O(N), SC : O(N+N)


# Method2 : Using Stack

def method2(s):

	stack = []
	word = ''

	for i in range(len(s)):
		if s[i]!=' ':
			word+=s[i]
		elif word :
			stack.append(word)
			word = ''
	if word:
		stack.append(word) # If we don't write this, The last word will not be added

	# u can replace the entire above code with One liner, stack = [i for i in s.split()]

	new_string = ''
	while(stack):
		new_string+=stack.pop()+ " "

	return new_string  #  TC : O(N), SC : O(N)


# Method 3: Reverse Each word in a string then Reverse the complete String

def method3(s):

	# function to reverse(st_ind,end)
	def reverse(s,st,end):

		s[st:end+1] = s[st:end+1][::-1]

	s = list(s)

	word_begin = -1

	for i in range(len(s)):

		if word_begin == -1 and s[i]!= ' ':
			word_begin = i 

		if word_begin != -1 and (i + 1 == len(s) or s[i + 1] == ' '):
 			reverse(s,word_begin,i)
 			word_begin = -1

	reverse(s,0,len(s))
	return ''.join(s)	 #  TC : O(N), SC : O(1)



if __name__=='__main__':

	string = input() # The world is beautiful just like my Mom

	new_string = method3(string)

	print(new_string)



