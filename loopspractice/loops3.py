largest_currently = -1
print('Before', largest_currently)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_currently :
        largest_currently = the_num
    print(largest_currently, the_num)
print('After', largest_currently)