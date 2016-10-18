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


lengthList = []
includeTitle = True
userInput = input("Include title when counting post length for questions? (Y/N): ")
if userInput == 'Y':
    includeTitle = True
else:
    includeTitle = False

for s in itemlist :
    if s.attributes['PostTypeId'].value == "1":         # For questions
        text = str(s.attributes['Body'].value) + "\r\n"
        text = strip_tags(text)
        text = html.unescape(text)
        tmp1 = text.split()                             # Get a list of words from body text of each question post

        if not includeTitle:
            #print(tmp1)
            #print(len(tmp1))
            lengthList.append(len(tmp1))                # Just append the body length

        else:
            #print(tmp1)
            #print(len(tmp1))

            text = str(s.attributes['Title'].value) + "\r\n"
            tmp2 = text.split()                         # If title included, also get list of words from title text
            #print(tmp2)
            #print(len(tmp2))

            lengthList.append(len(tmp1) + len(tmp2))    # Append the body and title length added together
            #print(len(tmp1) + len(tmp2))

for s in itemlist :
    if s.attributes['PostTypeId'].value == "2":         # For answers
        text = str(s.attributes['Body'].value) + "\r\n"
        text = strip_tags(text)
        text = html.unescape(text)
        tmp = text.split()                              # Get a list of words from body text of each answer post
        lengthList.append(len(tmp))

lengthList.sort()
#print(lengthList)
#print(len(lengthList))

increment = 0
total = 0
category = []
finalList = []
finalCount = []

while total < 1001:
    for x in lengthList:
        if (x >= increment * 50 + 1) and (x <= (increment + 1) * 50):   # if 0 to 50, then if 51 to 100, 101 to 150..
            total += 1
            category.append(x)
    increment += 1
    finalList.append(list(category))    # A list of lists for each category (0 to 50, 51 to 100 ... )
    category.clear()

for y in finalList:
    finalCount.append(len(y))           # For each list in final list, find the length then append to another list

increment = 0
for z in finalCount:                    # For display purposes
    print("Length " + str(increment*50+1) + " to " + str((increment + 1) * 50) + " : ", end="")
    print(str(z) + " posts")
    increment += 1