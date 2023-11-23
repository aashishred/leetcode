# The LeetCode Beginner's Guide
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > maximum:
                maximum = wealth
        return maximum
