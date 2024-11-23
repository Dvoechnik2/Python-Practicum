def main():
	start, end, step = map(float, input().split())
	while start <= end:
		print(f"{start:.2f}")
		start += step


if __name__ == "__main__":
	main()
