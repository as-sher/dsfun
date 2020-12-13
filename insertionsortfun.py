##You have been given an A array consisting of N integers. All the elements in this array are guaranteed to be unique. For each position i in the array A you need to find the position  should be present in, if the array was a sorted array. You need to find this for each i and print the resulting solution.

import string

n= int(input())
string = input()
array = string.split(" ")
num_array = []
num_array.append(int(array[0]))

for i in range(1,n):
    temp = int(array[i])
    free = True
    for j in range(0,i):
        if temp < num_array[j] and free:
            num_array.insert(j, temp)
            free = False
        elif j==(i-1) and free:
            num_array.append(temp)

print(num_array)

for i in range(0,n):
    temp = int(array[i])
    looking = True
    for j in range(0,n):
        if looking and temp == num_array[j]:
            print((j+1),end=' ')
            num_array[j] = 0 #note the specs give all nums > 0 so this allows non unique nums in array
            looking = False

print()