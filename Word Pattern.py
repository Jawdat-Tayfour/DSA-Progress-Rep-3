def WP(pattern:str,n:str):
    words = n.split(" ")
    if len(pattern) != len(words ):
        return False 
    charToWord  = {}
    wordToChar =  {}
    for c , w in zip(pattern,words):
        if c in charToWord and charToWord[c] != w:
            return False 
        if w in wordToChar and wordToChar[w] != c:
            return False 
        charToWord[c] = w 
        charToWord[w] = c 
    return True 
# Time complexity is O(n+m) , Space complexity is the same 
# sorry no solution from me today, I'm just too tired to think and I don't want to quit my daily practice, so, I'll just watch and write things. 
    