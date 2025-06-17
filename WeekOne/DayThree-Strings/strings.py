# Problem: Given two strings s and t, return True if t is an anagram of s, 
#  and False otherwise.
# An anagram is a word formed by rearranging the letters of another.


from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))