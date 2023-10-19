integer_list = [100,-100] # Change for different values
min_max = []

# Short Method - using sort()

#integer_list.sort()
#min_max.append(integer_list[0])
#min_max.append(integer_list[-1])
#print(min_max)


# longer method - no use of sort()

min_val = max_val = integer_list[0] # points both values to the start
    
for num in integer_list:
    if num < min_val: # compares if other number in list is smaller than current value
        min_val = num
    elif num > max_val: # compares if other number is larger
        max_val = num


min_max.append(min_val)
min_max.append(max_val)


print(min_max)