class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.count = 0

    def add(self, string: str, index: int) -> None:
        ptr = self
        for idx in range(index, len(string)):
            charIdx = ord(string[idx]) - ord('a')
            if ptr.childNode[charIdx] is None:
                ptr.childNode[charIdx] = TrieNode()
            ptr = ptr.childNode[charIdx]
            ptr.count += 1

    def remove(self, string: str, index: int) -> None:
        ptr = self
        for idx in range(index, len(string)):
            charIdx = ord(string[idx]) - ord('a')
            if ptr.childNode[charIdx] is None:
                ptr.childNode[charIdx] = TrieNode()
            ptr = ptr.childNode[charIdx]
            ptr.count -= 1

    def check(self, string: str, index: int) -> str:
        ptr, ans = self, ''
        for idx in range(index, len(string)):
            charIdx = ord(string[idx]) - ord('a')
            if ptr.childNode[charIdx] is None: return ans
            ans += string[idx]
            ptr = ptr.childNode[charIdx]
            if ptr.count < 1: return ans
        return string + string

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans, head = [], TrieNode()
        # Add all the strings to the trie
        for string in arr:
            for idx in range(len(string)):
                head.add(string, idx)
        for string in arr:
            res = string + string
            # remove the current string from trie
            for idx in range(len(string)):
                head.remove(string, idx)
            # iterate over each substring starting at i th and check for the uncommon string length
            for idx in range(len(string)):
                temp = head.check(string, idx)
                # store it in result if length is less or lexicographically smaller if equal
                if (len(temp) < len(res)) or (len(temp) == len(res) and temp < res):
                    res = temp
            # add res to final answer
            ans.append(res if len(res) <= len(string) else '')
            # add back the current string to the trie
            for idx in range(len(string)):
                head.add(string, idx)
        return ans