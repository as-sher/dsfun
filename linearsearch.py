n = int(input())
values = input()
key = int(input())

input_array = values.split(" ")

for j in range(n):
    if int(input_array[j]) == key:
        print("yes")
