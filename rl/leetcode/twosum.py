from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    mydict = dict()
    mylist = []
    for index in range(nums.__len__()):
        if (target - nums.__getitem__(index)) in mydict:
            mylist.append(mydict.get(target-nums.__getitem__(index)))
            mylist.append(index)
        mydict.update({nums.__getitem__(index):index})
    return mylist


print(twoSum([1,2,3], 5))
