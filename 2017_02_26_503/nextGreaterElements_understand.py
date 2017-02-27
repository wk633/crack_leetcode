# stack record indexes whose corresponding value is from large to small

def nextGreaterElements(nums):
    if not nums: return []
    stack, res = [], [None]*len(nums)
    for i in xrange(-len(nums), len(nums)):
        print i
        print "stack before: ", stack
        print "nums[i]: ", nums[i]
        while stack and nums[i] > nums[stack[-1]]:
            j = stack.pop()
            res[j] = nums[i]
        if i < 0:
            stack.append(i)
        print "stack: ", stack
        print "res: ", res
        print "\n"
    while stack:
        j = stack.pop()
        res[j] = -1
    return res
print nextGreaterElements([2,3,5,2,1])
