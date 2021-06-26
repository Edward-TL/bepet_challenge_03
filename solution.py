"""Solution by <USERNAME>."""


class Solution:
    """Solution to the duplicate zeros problem."""

    def duplicate_zeros(self, arr):
        """Modifies arr in place duplicating all zeros while maitining the original length."""
        # YOUR SOLUTION GOES HERE
        length = len(arr)

        for i in range(1, length):
            if arr[i] == 0 and arr[i -1] != 0:
                arr.insert(i, 0)
                arr.pop()

        return arr
