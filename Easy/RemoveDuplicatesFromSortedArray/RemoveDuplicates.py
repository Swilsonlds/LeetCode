# Given an integer array "nums" sorted in non-decreasing order, remove the duplicates
# in place such that each unique element only appears once. Return the number of unique elements
# in the array.

def remove_duplicates(nums: list[int]):
    l = 1
    for r in range(1, len(nums)):

        # if the array element r does not equal the element to it's left, it must be the first occurrence
        # of a new unique element, as the array elements are listed in non-decreasing order
        if nums[r] != nums[r - 1]:


            # The array element at the left pointer is set equal to the first occurrence of the unique value at nums[r]
            # and incremented by 1
            nums[l] = nums[r]
            l += 1

    return l

