def lengthOfLastWord(a):
	l = 0
	x = a.strip()
	for i in range(len(x)):
		if x[i] == " ":
			l = 0
		else:
			l += 1
	return l
print("The length of last word is",lengthOfLastWord("hello world"))
print("The length of last word is",lengthOfLastWord("fly me to the moon"))
print("The length of last word is",lengthOfLastWord("luffy is still joyboy"))
print("The length of last word is",lengthOfLastWord("123"))
print("The length of last word is",lengthOfLastWord("45&29 8*6^4"))
