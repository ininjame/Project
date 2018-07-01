import json,difflib #json is JavaScripObjectNotation, a data storage type used for transferring information
#difflib is library for sequence-matching and finding deltas between 2 strings
from difflib import get_close_matches, SequenceMatcher

data = json.load(open('data.json'))

def wordsearch(keyword):
    keyword = keyword.lower()
    def result(keyword):
        print('\n'+'Here are the definitions we found: ')
        for i in data[keyword]:
            print(str(data[keyword].index(i) + 1) + '. ' + i)
    if keyword in data:
        result(keyword)
    else:
        closematch = get_close_matches(keyword, data.keys())
        if closematch == []:
            print("This word doesn't exist. Please double check.")
        else:
            n=0
            for i in closematch:
                while True:
                    confirm = input('Did you mean "%s"? (y/n)\n' % i) #%s will be replaced with whatever is passed after the % inside the function.
                    if confirm == 'y':
                        result(str(i))
                        break
                    elif confirm == 'n':
                        n=n+1
                        break
                    else:
                        print('Wrong input. Please use only y for yes or n for no.')
                        continue
            if n == len(closematch):
                print('Sorry, word not found. Please try again.')

while True:
    keyword = input('Enter word, or press "e" to exit: ' + '\n')
    if keyword == "e":
        print('Exiting...')
        break
    else:
        wordsearch(keyword)
        print()
