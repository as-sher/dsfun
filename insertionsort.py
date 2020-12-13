## first code for insertion sort

initial_list = [31, 41, 59, 26, 41, 58]


for j in range(1, len(initial_list)):
    key = initial_list[j]
    i = j - 1
    while i>=0 and initial_list[i] > key:
        initial_list[i + 1]  = initial_list[i]
        i = i-1
    initial_list[i + 1] = key

print(*initial_list)



