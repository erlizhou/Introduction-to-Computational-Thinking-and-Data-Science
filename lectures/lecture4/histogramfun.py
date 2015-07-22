import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"
WORD_VOWELS = "aeiou"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    frequency = []
    for word in wordList:
        tot = 0.0
        for w in word:
            if w in WORD_VOWELS:
                tot += 1
        frequency.append(tot / len(word))

    pylab.figure(1)
    pylab.hist(frequency, numBins)
    pylab.title('Histogram of the proportion of vowels in each word of a wordList')
    pylab.ylabel('Number of words')
    pylab.xlabel('Proportion of vowels')
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
