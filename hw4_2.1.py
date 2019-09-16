'''
Yili Lin
3/5/2019
I have not given or received any unauthorized assistance on this assignment.
'''
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bs
from collections import Counter

class Collector(HTMLParser):
    '''collects hyperlink into a list'''

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = set()
        self.words = {}

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':  # collect HTTP URLs
                        self.links.add(absolute)

    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links

    def handle_data(self, data):
        'count the words in the web'
        new_words = data.split()
        for word in new_words:
            if word.isalpha():
                if word in self.words:
                    self.words[word]+=1
                else:
                    self.words[word]=1

    def returnwordlist(self):
        'return the words'
        return self.words

wordsdict= {}

def analyze(url):
    'returns list of http links in url, in absolute format'
    print('\n\nVisiting', url)
    global wordsdict
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()
    #get the dict and add to wordlist
    urlwordlist = collector.returnwordlist()
    X, Y = Counter(urlwordlist), Counter(wordsdict)
    wordsdict=dict(X+Y)
    #print(wordsdict)
    #sort the dict and get a list
    sortdict = sorted(wordsdict.items(), key=lambda item: item[1], reverse=True)
    common_25=(sortdict)[:25]# get the most 25
    print('\n{:10} {:10}'.format('word', 'count'))
    for count in common_25:
        # prin the most 25
        print('{:10} {:5}'.format(count[0], count[1]))
    return urls


visited = set() # initialize visited to an empty set

def crawl(url):
    '''a recursive web crawler that calls analyze()'''

    global visited
    #visit 500
    if len(visited)>500:
        return
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        if 'https://www.cdm.depaul.edu/' in link:
            if link not in visited:
                try:
                    crawl(link)
                except:
                    pass



crawl('https://www.cdm.depaul.edu/')

'''
word       count     
and        18737
the        17262
var        15043
to         12574
of          9119
CDM         5793
Admission   5719
if          5643
Web         5402
Strongly    5248
this        5060
for         4983
disagree    4951
agree       4951
function    4692
in          3980
a           3575
'''