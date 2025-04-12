"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
"""


def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
        first = second = -1
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num!= first:
                second = num
        return second if second!= -1 else -1

