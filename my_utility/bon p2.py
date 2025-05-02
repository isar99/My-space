arr1 = [1,2,3,4,5,6,7]
arr2 = [4,5,6,7]
target_value = -2

list1 = []
for pos1,num1 in enumerate(arr1):
	for pos2, num2 in enumerate(arr2):
		if arr1[pos1] - arr2[pos2] == target_value:
			list1.append([pos1,pos2])
		else:
			pass

if list1 == []:
	print([-1,1])

else:
	print(list1)