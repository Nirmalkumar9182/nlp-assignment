from xml.dom import minidom
import re
import html
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

xmldoc = minidom.parse('output.xml')

itemlist = xmldoc.getElementsByTagName('row') 
#print "Len : " len(itemlist)

# the regex for capturing ALL texts with angled brackets
# WE NEED TO IMPROVE THIS PART
# angled_bracket_pattern = r'\<[^>]*\>'

# this will PROBABLY help us pull posts with API mentions ONLY
api_mention_regex = re.compile(r'(\w+)((\.)\w+)*\(([^\s]*)(\s?,\s?[^\s]*)*\)')


api_count = 0
api_limit = 50
with open("50_posts_api_mentions_training.txt", "wb") as myfile:
    for s in itemlist :
            text = str(s.attributes['Body'].value)
            text = strip_tags(text)
            text = html.unescape(text)
            if api_mention_regex.search(text) is not None:
                # split a single post so that all new lines are removed from the post
                text = " ".join(text.split()) + "\r\n"
                myfile.write(text.encode('utf8'))
                api_count += 1

            if(api_count >= api_limit) :
                break

api_count = 0
iteration = 1
api_limit = api_limit + 3
# takes data after the training dataset            
with open("52_posts_api_mentions_test.txt", "wb") as myfile:
    for s in itemlist :
            text = str(s.attributes['Body'].value)
            text = strip_tags(text)
            text = html.unescape(text)
            if api_mention_regex.search(text) is not None:
                if api_count > api_limit:
                    # split a single post so that all new lines are removed from the post
                    text = " ".join(text.split()) + "\r\n"
                    myfile.write(text.encode('utf8'))
                api_count += 1

            if(api_count - api_limit >= api_limit) :
                break
