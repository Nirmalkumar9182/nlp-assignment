from xml.dom import minidom
xmldoc = minidom.parse('output.xml')

itemlist = xmldoc.getElementsByTagName('row') 
print "Len : ", len(itemlist)

with open("question.txt", "a") as myfile:

    for s in itemlist :
        if s.attributes['PostTypeId'].value == "1":
            myfile.write(s.attributes['Body'].value.encode('utf8') + "\r\n")

with open("answer.txt", "a") as myfile:

    for s in itemlist :
        if s.attributes['PostTypeId'].value == "2":
            myfile.write(s.attributes['Body'].value.encode('utf8') + "\r\n")
