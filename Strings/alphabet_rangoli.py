from string import ascii_lowercase as alp

def print_rangoli(size):
	line = []
	for i in range(size):
		s = '-'.join(alp[i:size])
		line.append(s[::-1] + s[1:])

	width = len(line[0])

	for i in range(size - 1, 0, - 1):
		print(line[i].center(width, '-'))
	for i in range(size):
		print(line[i].center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
