from xml.dom import minidom
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
angled_bracket_pattern = r'\<[^>]*\>'

questionCounter = 0
answerCounter = 0

for s in itemlist :
    if s.attributes['PostTypeId'].value == "1":         # For questions
        questionCounter += 1
    elif s.attributes['PostTypeId'].value == "2":
        answerCounter += 1

print("Question count: " + str(questionCounter))
print("Answer count: " + str(answerCounter))
