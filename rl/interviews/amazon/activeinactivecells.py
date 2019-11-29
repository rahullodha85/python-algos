def cellComplete(states, days):
    output = []
    start = 0
    end = 0
    for day in range(0, days):
        output = []
        for index in range(states.__len__()):
            # start of list
            if index == 0:
                if states[index + 1] == start:
                    output.append(0)
                else:
                    output.append(1)

            # end of list
            elif index == states.__len__() - 1:
                if states[index - 1] == end:
                    output.append(0)
                else:
                    output.append(1)
            # rest of elements
            else:
                if states[index - 1] == states[index + 1]:
                    output.append(0)
                else:
                    output.append(1)
        states = output

    return output

print(cellComplete([1,1,1,0,1,1,1,1], 2))