## reverse insertion sort

intial_list = [31, 41, 59, 26, 41, 58]

for j in  range(1, len(intial_list)):
    key = intial_list[j]

    i = j-1
    while i>=0 and intial_list[i] < key:
        intial_list[i + 1] = intial_list[i]
        i=i-1
    intial_list[i + 1] = key

print(*intial_list)



