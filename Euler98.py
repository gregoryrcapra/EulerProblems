# wrapper function and file handler
def anagramicSquares(file_path):
    with open(file_path,'r') as word_file:
        word_dict = findAnagrams(word_file)

    return maxAnagramicSquare(word_dict)


# adds anagrams to dictionary
def findAnagrams(word_file):
    word_dict = {}

    for word in word_file.read().split(','):
        trimmedWord = word[1:-1]
        sortedWord = ''.join(sorted(trimmedWord))
        if sortedWord not in word_dict:
            word_dict[sortedWord] = [trimmedWord]
        else:
            word_dict[sortedWord].append(trimmedWord)

    return word_dict


# for each anagram pair in dict, finds largest square
def maxAnagramicSquare(anagram_dict):
    maxAnagSquare = 0
    square_dict = {}

    for key,val in anagram_dict.items():
        if len(val) < 2:
            continue

        for i in range(len(val)):
            for j in range(i+1,len(val)):
                pairResult = examineSquares(val[i],val[j],square_dict)
                maxAnagSquare = max(maxAnagSquare,pairResult)

    return maxAnagSquare


# matches squares of same length to correct permutation
def examineSquares(word1,word2,square_dict):
    squareResult = 0

    if len(word1) not in square_dict:
        square_dict[len(word1)] = []
        square_base = math.floor(math.sqrt(10**(len(word1)-1)))

        while len(str(square_base**2)) <= len(word1):
            if len(str(square_base**2)) == len(word1):
                square_dict[len(word1)].append(square_base**2)
            square_base += 1

    for index,possibleMatch in enumerate(square_dict[len(word1)]):
        char_map = {}
        match = True

        for char in reversed(word1):
            currentDigit = possibleMatch % 10
            possibleMatch //= 10
            if char in char_map:
                if char_map[char] != currentDigit:
                    match = False
                    break
                else:
                    continue
            if currentDigit in char_map.values():
                match = False
                break
            char_map[char] = currentDigit

        if not match or (char_map[word2[0]] == 0):
            continue

        wordMatch2 = ''

        for char in word2:
            wordMatch2 += str(char_map[char])

        if int(wordMatch2) in square_dict[len(word1)]:
            squareResult = max(squareResult,square_dict[len(word1)][index],int(wordMatch2))

    return squareResult

# main entry point of program
if __name__ == '__main__':
    import time,math

    local_file_path = 'words.txt'
    start = time.time()
    print('Largest Anagramic Square: ',anagramicSquares(local_file_path))
    end = time.time()
    print('Total Run Time: ',end-start)
