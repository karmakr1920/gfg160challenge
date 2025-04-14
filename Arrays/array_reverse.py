"""
You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Constraints:
1<=arr.size()<=105
0<=arr[i]<=105
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""
def reverseArray(arr):
        # code here
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            # move 1 position from the left to right 
            left += 1
            # move 1 position from the right to left 
            right -= 1
        return arr
print(reverseArray([1,43,56,3,67,7]))