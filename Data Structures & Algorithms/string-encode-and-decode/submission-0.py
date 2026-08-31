class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))+'@'+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0

        while i < len(s):
            j=i

            # find #
            while s[j] != '@':
                j+=1

            # find length of word
            l = int(s[i:j])

            # get word
            word = s[j+1:j+1+l]

            res.append(word)
            i = j + 1 + l
        return res

        