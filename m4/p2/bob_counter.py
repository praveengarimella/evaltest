'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	s = raw_input()
	#your code here
	cnt = 0
	while "bob" in s:
		cnt += 1
		pos = s.find("bob")
		s = s[pos:pos + 4]
	print (cnt)

if __name__== "__main__":
	main()
