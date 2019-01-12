if __name__ == '__main__':
	n = int(input())
	
	students = {}
	for i in range(n):
		student = input().split()
		name, marks = student[0], student[1:]
		record = map(float, marks)
		avg = sum(record) / len(marks)
		students[name] = avg

	std = input()
	print('%.2f' %students[std])
