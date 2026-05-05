class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        word = list(s)
        i, j = 0, len(word) - 1

        while i < j:
            # find a vowel with i
            while i < j and word[i] not in vowels:
                i += 1

            while i < j and word[j] not in vowels:
                j -= 1

            word[i], word[j] = word[j], word[i]

            i += 1
            j -= 1

        return "".join(word)







s = "leetcode"
sol = Solution()
print(sol.reverseVowels(s))