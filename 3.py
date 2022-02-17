from linkedlist_helper import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        last_index = dict()
        # 目前为止无重复子串最大长度
        max_len = 0
        # 以当前扫描到的字符结尾的最大无重复子串长度
        cur_len = 0
        for i, c in enumerate(s):
            # c上次出现的位置
            last_seen = last_index.get(c)
            # c之前没出现过，加入c仍然是无重复的
            if last_seen is None:
                cur_len += 1
            else:
                # 到上次出现的位置的距离
                diff = i - last_seen
                # 上次出现过的位置并不在当前无重复子串中，则直接加入e
                if diff > cur_len:
                    cur_len += 1
                # 上次出现过的位置在当前无重复子串中，更新当前无重复子串
                else:
                    cur_len = diff
            last_index[c] = i
            if cur_len > max_len:
                max_len = cur_len
        return max_len


for t in ["pwwkew", 'abc', 'aaaa', 'abcad', ]:
    print(t, Solution().lengthOfLongestSubstring(t))
