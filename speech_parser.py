__author__ = 'shekhargulati'

import nltk


def text_from_url(url, min_word_length=4):
    from urllib import urlopen

    raw_text = urlopen(url).read()
    tokens = nltk.word_tokenize(raw_text)
    print "Tokens ", len(tokens)
    tokens_without_punc = [token.lower() for token in tokens if token.isalpha() and len(token) > min_word_length]
    text = nltk.Text(tokens_without_punc)
    return text


def fd_words(url):
    text = text_from_url(url)
    return nltk.FreqDist(text)


def words_usage(url, word):
    """
    This method shows how a word is used in a text
    """
    text = text_from_url(url, min_word_length=0)
    return text.findall("<.*><.*><" + word + ">")


speech_url = 'https://raw.githubusercontent.com/shekhargulati/corpus/master/15th-august-speeches/2014.txt'

# fd = fd_words('https://raw.githubusercontent.com/shekhargulati/corpus/master/15th-august-speeches/2014.txt')
# top_50_words = fd.keys()[0:50]
# for word in top_50_words:
#     print "{'word': '%s', 'count' : %d}," % (word, fd[word])
# fd.tabulate(50)

wordlist = words_usage(speech_url, "corruption")
print(wordlist)







