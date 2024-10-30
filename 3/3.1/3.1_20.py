import math


def main():
	s = input().split()
	stack = []
	for x in s:
		if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
			stack.append(int(x))
		elif x == '+':
			b, a = stack.pop(), stack.pop()
			stack.append(a + b)
		elif x == '-':
			b, a = stack.pop(), stack.pop()
			stack.append(a - b)
		elif x == '*':
			b, a = stack.pop(), stack.pop()
			stack.append(a * b)
		elif x == '/':
			b, a = stack.pop(), stack.pop()
			stack.append(a // b)
		elif x == '~':
			a = stack.pop()
			stack.append(-a)
		elif x == '!':
			a = stack.pop()
			stack.append(math.factorial(a))
		elif x == '#':
			a = stack.pop()
			stack.append(a)
			stack.append(a)
		elif x == '@':
			c, b, a = stack.pop(), stack.pop(), stack.pop()
			stack.append(b)
			stack.append(c)
			stack.append(a)
	print(stack[0])


if __name__ == "__main__":
	main()
