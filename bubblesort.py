a = []
for i in range(0,10):
	new_element = int(input())
	a.append(new_element)
i = 0
for i in range(0,10):
	for j in range(0,9-i):
		if a[j]>a[j+1]:
			temp = a[j+1]
			a[j+1] = a[j]
			a[j] = temp

print(b)
