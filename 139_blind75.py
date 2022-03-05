from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_len = max(len(w) for w in wordDict)
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            if i == 0:
                if s[i] in wordDict:
                    dp[i] = True
                continue
            for j in range(i, max(-1, i - max_word_len), -1):
                w = s[j: i + 1]
                if (j == 0 or dp[j - 1]) and w in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


print(Solution().wordBreak('leetcode', ['leet', 'code']))
print(Solution().wordBreak('applepenapple', ["apple", "pen"]))
print(Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
