class Solution:
    def isPalindrome(self, s: str) -> bool:
        out=[]
        for char in s:
            if char.isalnum():
                lc=char.lower()
                out.append(lc)
        outstr="".join(out)
        return outstr==outstr[::-1]

        