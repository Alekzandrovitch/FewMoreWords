import requests

#
#DataMuse
# words related to duck that start with the letter b	/words?ml=duck&sp=b*
#DAta must has no dictionary must find new sauce
def Dictionary(word):
    srch = str(word)
    x = urllib.request.urlopen("http://dictionary.reference.com/browse/" + srch + "?s=t")
    x = x.read()
    x = x.content()
    items = re.findall('<div class="def-content">',x)
    print(x)

def Noun(word):
    searchLink = 'http://api.datamuse.com/words?rel_jja='+word
    a  = search(searchLink)
    return a


def ReverseDictionary(word):
    sentence = []
    sentence = word.split()
    print(sentence)
    x  =0
    while x < len(sentence) :
        if x % 2 != 0 and x != 0:
            sentence.insert(x,'+')
        x+=1
    x = 0
    sentence.insert(0,'http://api.datamuse.com/words?ml=')
    sentence_2 = ''
    while x < len(sentence):
        sentence_2 = sentence_2 + sentence[x]
        x+=1

    searchLink =  'http://api.datamuse.com/words?ml='+sentence_2
    a = search(searchLink)
    return a
#
# words that sound like elefint	/words?sl=elefint
def Sound(word):
    searchLink = 'http://api.datamuse.com/words?sl='+word
    a = search(searchLink)
    return a
#
# words that start with t, end in k, and have two letters in between
# 	/words?sp=t??k
def Spelled(word):

    searchLink = 'http://api.datamuse.com/words?sp='+word
    a = search(searchLink)
    return a
#
# words that rhyme with forgetful	/words?rel_rhy=forgetful
def StartWithAndRelated(word):
    words = word.split()
    searchLink = 'http://api.datamuse.com/words?ml='+words[1]+'&sp='+words[0]+'*'
    a  = search(searchLink)
    return a
def EndWithAndRelated(word):
    words = word.split()
    searchLink = 'http://api.datamuse.com/words?ml='+words[1]+'&sp=*'+words[0]
    a  = search(searchLink)
    return a
def RhymeAndRelated(word):
    words = word.split()
    searchLink = 'http://api.datamuse.com/words?ml='+words[0]+'&rel_rhy='+words[1]
    a  = search(searchLink)
    return a
def Rhyme(word):
    searchLink = 'http://api.datamuse.com/words?rel_rhy='+word
    a  = search(searchLink)
    return a
#
# adjectives that are often used to describe ocean
# /words?rel_jjb=ocean
def Adjective(word):
    searchLink = 'http://api.datamuse.com/words?rel_jjb='+word
    a = search(searchLink)
    return a

def search(url):
    r = requests.get(url)
    parsed = r.json()
    #print(parsed)
    return parsed
