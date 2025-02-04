"""
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have.
 You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
"""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        return sum(1 for x in stones 
        if x in jewels )
    
    