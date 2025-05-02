daily_sales = input("Enter the daily sales: ")
sl_num = int(input("Total number shortlisted: "))
sl_sales = input("shortlisted sales: ")

sum = 0
for l in sl_sales:
	sum += ord(l)*daily_sales.count(l)

print(sum)