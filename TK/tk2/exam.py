"""."""


def count_clumps(nums: list):
    """."""
    counter = 0
    for i in range(len(nums)):
        if len(nums) == 1:
            return 0
        elif i == 0:
            if nums[i] == nums[i + 1]:
                counter += 1
            else:
                continue
        elif i == len(nums) - 1:
            return counter
        elif nums[i - 1] != nums[i] and nums[i] == nums[i + 1]:
            counter += 1
    return counter
