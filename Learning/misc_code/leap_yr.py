def leap():
	year = int(input())

	if year % 4 == 0:
		if year % 400 ==0:
			return True
		elif year % 100 == 0:
			return False
		return True
	else:
		return False

if __name__ == "__main__":
	leap()
