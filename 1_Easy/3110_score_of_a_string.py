"""
You are given a string s. The score of a string is defined as the sum of the 
absolute difference between the ASCII values of adjacent characters.

Return the score of s.

Example 1:

Input: s = "hello"
Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 
= 13.

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""
class Solution(object): 
    def scoreOfString(self, s): 
        """
        :type s: str
        :rtype: int
        """
        score = 0 # Initializing the score
        for i in range(1, len(s)): # Looping through every character
            score += abs(ord(s[i]) - ord(s[i -1])) # Calculating the score
        return score

solution = Solution() # Creating an object
s = "zaz" 
print(solution.scoreOfString(s)) # Calling the object method and printing the solution