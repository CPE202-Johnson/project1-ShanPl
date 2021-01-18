# string --> list of strings
# purpose generate all permutations of a string and add them to a list
def perm_gen_lex(word): # ex: word = 'abc'
    if len(word) <= 0:
        return [''] #[]
    if len(word) == 1: 
        #return single letter in the form of a list with a single string
        return [word] #['a']
    index = 0
    all_words = [] #all_words is a list of strings
    while index < len(word): #'abc'
        letter = word[index] #'a'
        #remove a letter at index
        shorter_word = word[:index] + word[index+1:] # 'bc'
        permutation = perm_gen_lex(shorter_word) # ['bc', 'cb']
        i = 0
        #insert the letter in every possible place and add each word to all_words
        while i < len(permutation):
            permutation[i] = letter + permutation[i] #i=0: 'abc', i=1: 'acb'
            all_words.append(permutation[i]) #['abc', 'acb']
            i+= 1
        index += 1
    return all_words #['abc, acb, bac, bca, ...']
print(perm_gen_lex(''))