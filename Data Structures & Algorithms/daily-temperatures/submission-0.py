class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stemp,sindex=stack.pop()
                temp[sindex]=i-sindex
            stack.append([t,i])
        return temp