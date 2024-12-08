# Sort string with num words 

# Given a String with a number in it we have sort the string based on the number
def func(word):
    for char in word:
        if char.isdigit():
            return int(char)
    return float('inf')
s = input() # Stri3ng ca1n 2be sorted5 us0ing t6his co5de

words = s.split()

s_arr = sorted(words, key = func)

print(" ".join(w for w in s_arr)) # us0ing ca1n 2be Stri3ng sorted5 co5de t6his