class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=sorted(zip(position,speed),reverse=True)
        stk=[]
        for p,s in pairs:
            time=(target-p)/s
            if not stk or time>stk[-1]:
                stk.append(time)
        return len(stk)