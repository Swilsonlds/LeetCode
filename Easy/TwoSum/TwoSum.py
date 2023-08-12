# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums: list[int], target: int) -> list[int]:

    prevMap = {} # value -> index


    for index, value in enumerate(nums):  

    # For each element in the list, we will subtract the element from the target. This difference
    # will be the number we would add to the current element to reach the target
        difference = target - value  

        # Here we check to see if the difference is currently in our hashmap. If it is, we return the index of the current index
        # along with the index of the difference from the hashmap
        if difference in prevMap:
            return [prevMap[difference], index]
        
        # If the difference between the target value and the current element is not currently in the array
        # we map the current elements value to its index in the hashmap and continue to iterate through
        # the list
        prevMap[value] = index

