'''Question: Maximum Points You Can Obtain from Cards -> leetcode 1423

You are given an integer array cardPoints and an integer k.
In one move, you can take a card either from the beginning or the end of the array. You must take exactly k cards.
Return the maximum score you can obtain.
Example
Input:
cardPoints = [1,2,3,4,5,6,1]
k = 3
Output:
12
Explanation:
Take the last three cards: 6 + 5 + 1 = 12'''


class Solution(object):
    def maxScore(self, card, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left_sum = 0
        max_sum = 0 
        right_sum = 0 
        r = len(card) - 1

        for i in range(k):
            left_sum = left_sum + card[i]
            max_sum = left_sum

        for i in range(k - 1,-1,-1):
            left_sum = left_sum - card[i]
            right_sum = right_sum + card[r]
            r-=1
            max_sum = max(max_sum,left_sum + right_sum)

        return max_sum

        