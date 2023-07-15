"""
Author: Wasim
This method will generate all the combinations of the given input string.
Ex:
    input:"abc"
    output:['a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac', 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
"""

def combinations(nums,combs):
    """
    This is a recursive method in with combination functionality.
    """
    if combs:
        result.append("".join(combs))
    if len(combs)==len(nums):
        return
    else:
        for i in range(len(nums)):
            val=nums[i]
            combs.append(nums[i])
            combinations(nums[:i]+nums[i+1:],combs)
            combs.pop()
    return result
result=[]
nums="abc"
combinations(nums,[])
print(result)