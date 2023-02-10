def maxwords(sentences):
    max_words=0
    for sentence in sentences:
        words=sentence.split()
        max_words=max(max_words,len(words))
    return max_words
sentences=("enter array of string sentences")
print ("the maximum number of words that appear in a sentences is",maxwords(sentences))
