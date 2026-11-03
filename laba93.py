from collections import Counter
def scramble(s1, s2):
    if len(s2) > len(s1):
        return False 
    count1 = Counter(s1)
    count2 = Counter(s2)
    for char, needed in count2.items():
        if count1[char]<needed:
            return False
    return True