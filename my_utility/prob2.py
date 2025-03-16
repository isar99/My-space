arr = []


N = int(input("Enter the number of command: "))
print("Commands: ")
for n in range(N):
	action_values = input().split()
	if len(action_values) > 1:
		action, values = action_values[0], map(int, action_values[1:])
	else:
		action = action_values[0]

	if action == 'print':
		print(arr)
	elif action == 'append':
		arr.append(values)
	elif action == 'insert':
		arr.insert(int(action_values[1]),int(action_values[2]))
	elif action == 'sort':
		arr.sort()
	elif action == 'pop':
		arr.pop()
	elif action == 'remove':
		arr.remove(values)
	elif action == 'reverse':
		arr.reverse()