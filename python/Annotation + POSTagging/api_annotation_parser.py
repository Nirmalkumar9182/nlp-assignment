import re
import nltk
import spacy
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import StanfordTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer

# pre-load spacy's library
# takes about 30 seconds to load
# nlp = spacy.load('en')

# using regex to tokenize
#p = re.compile(r"(((\w+)((\.)\w+)*\(([^\s]*)(\s?,\s?[^\s]*)*\))|(\w+(?:[-']\w+)+|'|[-.(]+|\S\w*))")

''' tokenizes
1) string values
2) string ending with a '(' e.g. strin(
3) function() purely with no parameters
'''
#expre = "(((\w+)((\.)\w+)*\(\)?)|,|\w+(?:[-']\w+)+|'|[-.(]+|\S\w*)"
expre = "\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"
p = re.compile(expre)
re_tokenizer = RegexpTokenizer(expre)

wordList = []
annotateList = []

annotate = True

fname = input("Enter the file name to open (without extensions): ")

# load into spacy's nlp object
# doc = nlp(open(fname + '.txt', 'r', encoding='utf8').read())

s = open(fname + '.txt', 'r', encoding='utf8').read()

with open(fname + '.txt', 'r', encoding='utf8') as fp:
    for line in fp:
        # only using finditer was i able to obtain the results without greedy search
        # the function returns an iteratable so we have to use a for loop on it
        for x in re.finditer(p, line):
            # x.group(0) contains the regex matched expression
            wordList.append(x.group(0))

posTagList = nltk.pos_tag(wordList)
annotateIndexes = []

with open(fname + '.ann', 'r', encoding='utf8') as fp:
    for line in fp:
        wordArr = line.split("\t")
        indices = wordArr[1].split(" ")
        annotateIndexes.append(indices)

wordSpanIndex = list(re_tokenizer.span_tokenize(s))

index = 0

if not annotate:
    annotateList = posTagList

while index < len(posTagList) and annotate:                    
    x = posTagList[index]
    annotated = False

    totalNewlines = s[0:wordSpanIndex[index][0]].count('\n\n')
    spanStart = wordSpanIndex[index][0] # + totalNewlines
            
    for annotateObj in annotateIndexes:
        tag = annotateObj[0]
        startIndex = int(annotateObj[1])
        endIndex = int(annotateObj[2])

        if spanStart in range(startIndex, endIndex):
            annotated = True
            annotateList.append( x + (tag ,))
            break

    if not annotated:
        annotateList.append( x + ("O", ))
    
    index += 1

for t in range(0,2):
    lineCount = 0
    if t == 0 :
        annotate = True
        file_type = "_training"
    else :
        annotate = False
        annotateList = posTagList
        file_type = "_test"
        
    with open(fname + file_type + ".txt", "wb") as myfile:
        for x in annotateList:
            if(lineCount > 0 and lineCount % 11 == 0):
                myfile.write("\t\t\n".encode('utf8'))
                
            if(annotate):
                string = str(x[0]) + "\t" + x[1] + "\t" + x[2] + "\n"
                myfile.write(string.encode('utf8'))
            else:
                string = str(x[0]) + "\t" + x[1] + "\n"
                myfile.write(string.encode('utf8'))

            lineCount += 1


print("Annotation complete.")

print("done")
