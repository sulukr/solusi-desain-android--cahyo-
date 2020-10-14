# Program 1 - Sorting

array = [4,9,7,5,8,9,3]

counter = 0
num = len(array)
for i in range(num):
    for j in range(i+1, num):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            counter = counter + 1

print("sort = ", array)
print("jumlah swap = ", counter)
