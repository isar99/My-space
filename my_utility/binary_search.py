#1,2,3,4,5,6,7,8,9,10
def binary_search(num,sorted_num):
	low_index = 0
	high_index = len(sorted_num)-1
	return binary_search_x(num,sorted_num,low_index,high_index)

def binary_search_x(num,sorted_num,low_index,high_index):
	if low_index > high_index:
		return -1
	mid_index = (low_index + high_index)/2
	if num < sorted_num[mid_index]:
		return binary_search_x(num,sorted_num,low_index,mid_index)
	elif num > sorted_num[mid_index]:
		return binary_search_x(num,sorted_num,mid_index,high_index)
	elif num == sorted_num[mid_index]:
		return mid_index