"""
Author: Wasim
This method will generate all the permutations of the given input string.
Ex:
    input:"abc"
    output:['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""

def permutations(nums,combs):
    """
    This is a recursive method in with combination functionality.
    """
    # if combs:
    #     result.append("".join(combs))
    if len(combs)==l and "".join(combs) not in result:
        result.append("".join(combs))
        return
    else:
        for i in range(len(nums)):
            val=nums[i]
            combs.append(nums[i])
            permutations(nums[:i]+nums[i+1:],combs)
            combs.pop()
    return result
result=[]
nums="abc"
l=len(nums)
permutations(nums,[])
print(result)
print(len(result))