class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

        # final = []
        # visited = set()

        # for word in strs:
        #     if word in visited:
        #         continue
        #     else:
        #         sublist = []
        
        #         hash1 = {}

        #         for char in word:
        #             if char in hash1:
        #                 hash1[char] += 1
        #             else:
        #                 hash1[char] = 1

        #         sublist.append(word)
        #         visited.add(word)

        #         for newword in strs:
        #             if newword in visited:
        #                 continue

        #             if len(newword) == len(word):
        #                 hash2 = {}
        #                 for char in newword:
        #                     if char in hash2:
        #                         hash2[char] += 1
        #                     else:
        #                         hash2[char] = 1
        #                 if hash1 == hash2:
        #                     sublist.append(newword)
        #                     visited.add(newword)
        #         final.append(sublist)
        # return final
