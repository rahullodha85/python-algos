def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    # WRITE YOUR CODE HERE

    largest = -1  # for comparison with largest sum
    output = []  # placeholder return val
    temp_list = []
    for fore_index in range(foregroundAppList.__len__()):
        for back_index in range(backgroundAppList.__len__()):
            test = foregroundAppList[fore_index][1] + backgroundAppList[back_index][1]
            if test <= deviceCapacity and test >= largest:
                temp_tupple = tuple((foregroundAppList[fore_index][0], backgroundAppList[back_index][0],
                                                     test))  # tupple of pair and sum
                largest = test
                temp_list.append(temp_tupple)

    for item in temp_list:
        if item.__getitem__(2) >= largest: # compare to most optimized memory
            temp = []
            temp.append(item.__getitem__(0))
            temp.append(item.__getitem__(1))
            output.append(temp)
    if output.__len__() == 0:
        temp = []
        output.append(temp)

    return output


print(optimalUtilization(10, [[1,3],[2,5],[3,7],[4,10]], [[1,2],[2,3],[3,4],[4,5]]))
print(optimalUtilization(7, [[1,2],[2,4],[3,6]], [[1,2]]))
print(optimalUtilization(16, [[2,7],[3,14]], [[2,10],[3,14]]))