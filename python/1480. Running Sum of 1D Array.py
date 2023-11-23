# The LeetCode Beginner's Guide
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = 0
        answer = []
        for num in nums:
            runningSum += num
            answer.append(runningSum)
        return answer
