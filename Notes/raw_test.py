new_array=[1,2,3,4]
power_set=[[]]
for x in new_array:
    for i in range(len(power_set)):
        tmp_list = power_set[i].copy()
        tmp_list.append(x)
        power_set.append(tmp_list)
print(power_set)