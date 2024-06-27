"""This module define function for AIO2024 Module 1 week 2 exercise."""
import collections
#brute force: create 2 pointers, left and right.The incrementation of left and right pointer is same
# Complexity: O(n * k)
def sliding_window(nums: list[int],k: int) -> list[int]:
    """Find maximum value in a defined sliding window

    Args:
        nums (list[int]): given array
        k (int): window length

    Returns:
        list[int]: List of maximum value in each iteration of sliding window
    """
    arr: list[int] = []
    for left in range(len(nums) - k + 1):
        right = k + left
        max_value = max(nums[left : right])
        arr.append(max_value)
    print(arr)
    return list(arr)

nums_list = [3,4,5,1,-44,5,10,12,33,1]
SIDE = 3
sliding_window(nums_list,SIDE)

#deque:

def sliding_window_deque(nums: list[int],k:int) -> list[int]:
    """Find ding maximum value in sliding window using deque

    Args:
        nums (list[int]): list of interger
        k (int): sindow side

    Returns:
        output (list[int]): list of maximum value in each iteration
    """
    output: list[int] = []
    left = right = 0 #create 2 pointer to track the sliding window
    q: collections.deque[int] = collections.deque[int]()
    # create a deque to store indice for each iteration of a window

    while right < len(nums): #ensure the right pointer is lower than len to stop the window
        while q and nums[q[-1]] < nums[right]:
            #num[q[-1]]: the last value of a deque represent index in nums
            q.pop()
#when right pointer value in nums greater than value in index stored in q, pop it
        q.append(right) # append the index if condition is not met

        if left > q[0]:
        #if the left pointer is greatet than index storerd in q, pop
            q.popleft()
        if right + 1 >= k:
        #if right pointer + 1 is greater than the side of window, append the first value in q
        # the deque always sort as decreasing order so append 1st value in q to output
            output.append(nums[q[0]])
            left += 1
        right += 1
    return output
