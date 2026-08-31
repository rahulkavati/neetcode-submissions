class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # final = [0]*len(temperatures)
        # for i, n in enumerate(temperatures):
        #     for k,j in enumerate(temperatures):
        #         if k>i:
        #             if j>n:
        #                 final[i]=k-i
        #                 break
        # return final    

        result = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i-j
            stack.append(i)
        return result