"""Solution by <USERNAME>."""


class Solution:
    """Solution to the duplicate zeros problem."""

def duplicate_zeros(self, arr):
    """Modifies arr in place duplicating all zeros while maitining the original length."""
    # YOUR SOLUTION GOES HERE
    arr = [1,0,2,3,0,4,5,0]
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i+1,0)
            del arr[len(arr)-1]
            i = i + 2
        else:
            i = i + 1
    print(self,arr)