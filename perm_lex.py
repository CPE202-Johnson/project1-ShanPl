# string --> list of strings
# purpose generate all permutations of a string and add them to a list
def perm_gen_lex(word): # ex: word = 'abc'
    if len(word <= 0):
        return [] #[]
    if len(word) == 1: 
        #return single letter in the form of a list with a single string
        return [word] #['a']
    if len(word) == 2:
        # create a list of the two letters in order (word) and backwards (new_word) 
        new_word = [word[1] + word[0]] #['ba']
        two_words = [word] + new_word #['ab', 'ba']
        return two_words 
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

'''
    abcd
        bcd
            cd 
            return ['cd', 'dc']
        list = ['cd', 'dc']
        new_list = ['bcd', 'bdc']
        append to total list
            bd
            ['bd', 'db']
        list = ['bd', 'db']
        new_list = ['cbd', 'cdb']
        append to total list
            bc
        new_list = 
        append to total list
    list = ['bcd', 'bdc', 'cbd', 'cdb', '
    new_list = ['abcd', 'abdc', 'acbd', 'acdb', '
''' 
        
print (perm_gen_lex('abcd'))

# word = 'abc'
# index = 0
# word = word[:index] + word[index+1:]
# print(word)