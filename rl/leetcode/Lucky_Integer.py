""" 
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""


class Solution:
    def findLucky(self, arr) -> int:
        max_val = -1
        if len(arr) < 1:
            return max_val
        d = {}
        # get val-freq kv pair dict
        for x in arr:
            if x in d:
                d.update({x: d[x] + 1})
            else:
                d.update({x: 1})

        vals = []

        for key in d.keys():
            if key == d[key]:
                vals.append(key)

        if len(vals) == 0:
            return max_val
        for x in vals:
            max_val = max(x, max_val)

        return max_val
