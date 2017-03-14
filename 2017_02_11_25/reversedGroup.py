# @author: wang633kai
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        resultDict = collections.defaultdict(list)
        for item in strs:
            resultDict["".join(sorted(item))].append(item)
        return [item for item in resultDict.values()]


        # result = []
        # strDict = collections.defaultdict(list)
        # for idx,value in enumerate(strs):
        #     strDict[''.join(sorted(value))].append(idx)
        # for k in strDict:
        #     result.append([strs[item] for item in strDict[k]])
        # return result
