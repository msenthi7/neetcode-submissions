class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=temperatures
        stack=[]
        n=len(temps)
        res=[0]*n
        for i,t in enumerate(temps):
            while stack and stack[-1][0]<t:
                stackt,stacki=stack.pop()
                res[stacki]=i-stacki
            stack.append((t,i))
        return res


        