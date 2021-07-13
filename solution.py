"""Solution by <USERNAME>."""


class Solution:
    """Solution to the duplicate zeros problem."""

    def duplicate_zeros(self, arr):
        """Modifies arr in place duplicating all zeros while maitining the original length."""
        # YOUR SOLUTION GOES HERE
        z=1
        vol=True
        x=len(arr)
        for cont in range(x):
            if z!=1:
                if vol==False:
                    z=1
                    continue
            if arr[cont]==0:
                arr.insert(cont,0)
                arr.pop()
                vol=False
                z=0
        return arr
