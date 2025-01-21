# Word Ladder
'''Given a WordList containing a List of words, and two strings beginWord and endWord.
 We need to cal minimum transformation to make beginWord to endWord.

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. 
**Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, 
or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

'''
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, startWord: str, targetWord: str, wordList: List[str]) -> int:
        queue = deque([(startWord, 1)])
        wordSet = set(wordList)
        wordSet.discard(startWord)

        while queue:
            word, steps = queue.popleft()

            if word == targetWord:
                return steps

            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i] + ch + word[i+1:]  

                    if newword in wordSet:
                        wordSet.discard(newword)  
                        queue.append((newword, steps + 1))
        return 0 

if __name__ == '__main__':
	
	obj = Solution()

	wordList = ["hot","dot","dog","lot","log","cog"]
	startWord =  "hit"
	targetWord =  "cog"

	cnt = obj.ladderLength(startWord,targetWord,wordList)
	print(f'No of transformations : {cnt}')