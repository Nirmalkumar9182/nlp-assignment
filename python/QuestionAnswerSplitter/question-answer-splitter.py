from xml.dom import minidom
import re

xmldoc = minidom.parse('output.xml')

itemlist = xmldoc.getElementsByTagName('row') 
print "Len : ", len(itemlist)

angled_bracket_pattern = r'\<[^>]*\>'

with open("question_without_angle.txt", "a") as myfile:

    for s in itemlist :
        if s.attributes['PostTypeId'].value == "1":
            text = s.attributes['Body'].value.encode('utf8') + "\r\n"
            text = re.sub(angled_bracket_pattern, "", text)
            myfile.write(text)

with open("answer_without_angle.txt", "a") as myfile:

    for s in itemlist :
        if s.attributes['PostTypeId'].value == "2":
            text = s.attributes['Body'].value.encode('utf8') + "\r\n"
            text = re.sub(angled_bracket_pattern, "", text)
            myfile.write(text)
