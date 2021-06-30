"""Solution by <USERNAME>."""


class Solution:
    """Solution to the duplicate zeros problem."""

    def duplicate_zeros(self, arr):
        """Modifies arr in place duplicating all zeros while maitining the original length."""
        # YOUR SOLUTION GOES HERE
        x=len(arr)
        vol=True
        for cont in range(x):
            if vol==False:
                continue
            if arr[cont]==0:
                arr.insert(cont,0)
                arr.pop()
                vol=False
            return arr
