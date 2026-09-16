class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I can by brute force, check each string if they have an       anagram, and if so, group them together. This means
        # I have to check same string twice.
        # If I rather map strings with same characters in hashmap, it will auto group them. But keys in a hashmap can anything other than set, list or dict
        # Storing the string itself as a key won't group anagrams: because the order of the letters is different, "ant" and "tan" are treated as completely distinct keys.
        # Thus we can use Tuple (immutable)
        # Instead, we use the count of characters (mapped to alphabet positions) as a tuple key. This key will have str groupewd in list, which cna finally be aggregated.
        anagm=defaultdict(list)
        for s in strs:
            count=[0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            key=tuple(count)
            anagm[key].append(s)
        return list(anagm.values())






        