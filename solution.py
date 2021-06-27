"""Solution by <USERNAME>."""


class Solution:
    """Solution to the duplicate zeros problem."""

    def duplicate_zeros(self, arr):
        """Modifies arr in place duplicating all zeros while maitining the original length."""
        # YOUR SOLUTION GOES HERE

        acc = 0

        while acc < len(arr):
            if arr[acc] == 0:
                arr.insert(acc, 0)
                arr.pop()
                acc += 1
            acc += 1

        return arr
