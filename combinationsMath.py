"""
Author:Wasim
Program to generate mathematical combinations of the string.
Ex:
    input:"abc"
    output":['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
"""
def combinations(combinationArray,combs):
    combs=sorted(combs)
    if "".join(combs) not in result:
        # print(combinationArray,combs)
        result.append("".join(combs))
    if not combinationArray:
        return
    elif len(combs)==l:
        return
    else:
        for  i in range(len(combinationArray)):
            val=combinationArray[i]
            combs.append(val)
            combinations(combinationArray[:i]+combinationArray[i+1:],combs)
            combs.pop()
input="abc"
result=[]
l=len(input)
# for i in range(len(input)):
combinations(input,[])
print(result)
print(len(result))