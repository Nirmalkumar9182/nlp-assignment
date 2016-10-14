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
angled_bracket_pattern = r'\<[^>]*\>'

with open("question_without_angle.txt", "wb") as myfile:
    for s in itemlist :
        if s.attributes['PostTypeId'].value == "1":
            text = str(s.attributes['Body'].value) + "\r\n"
            text = strip_tags(text)
            text = html.unescape(text)
#            text = re.sub(angled_bracket_pattern, "", text)
            myfile.write(text.encode('utf8'))

with open("answer_without_angle.txt", "wb") as myfile:
    for s in itemlist :
        if s.attributes['PostTypeId'].value == "2":
            text = str(s.attributes['Body'].value) + "\r\n"
            text = strip_tags(text)
            text = html.unescape(text)
#            text = re.sub(angled_bracket_pattern, "", text)
            myfile.write(text.encode('utf8'))

