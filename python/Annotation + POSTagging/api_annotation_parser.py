import re
import nltk

# using regex to tokenize
#p = re.compile(r"(((\w+)((\.)\w+)*\(([^\s]*)(\s?,\s?[^\s]*)*\))|(\w+(?:[-']\w+)+|'|[-.(]+|\S\w*))")

''' tokenizes
1) string values
2) string ending with a '(' e.g. strin(
3) function() purely with no parameters
'''
#p = re.compile(r"(((\w+)((\.)\w+)*\(\)?)|(\w+(?:[-']\w+)+|'|[-.(]+|\S\w*))")
p = re.compile(r"(((\w+)((\.)\w+)*\(\)?)|,|\w+(?:[-']\w+)+|'|[-.(]+|\S\w*)")

wordList = []
annotateList = []


filetext = open('50_posts_api_mentions.txt', 'r', encoding='utf8').read()

# only using finditer was i able to obtain the results without greedy search
# the function returns an iteratable so we have to use a for loop on it
for x in re.finditer(p, filetext):
    # x.group(0) contains the regex matched expression
    wordList.append(x.group(1))

posTagList = nltk.pos_tag(wordList)
# print(nltk.pos_tag(wordList))

u = re.compile(r"((\w+)((\.)\w+)*\(\))")
b = re.compile(r"((\w+)((\.)\w+)*\()")

index = 0

# annotation loop
while index < len(posTagList):
    x = posTagList[index]
    tag = ('O', )
    
    # if string matches U tag, just tag a U
    if(u.match(wordList[index]) or (index+1 < len(wordList) and wordList[index+1] == "function" ) ):
        tag = ('U-API',)
    # if string contains an open bracket at the end
    elif(b.match(wordList[index])):
        # start to evaluate for a close bracket
        anchor = index
        scanner = anchor
        
        # we have a scanner to run through the array of text until we find a close bracket
        # we may have to implement a limit for the scanner to run to since it is impossible to have X amount of parameters
        # for a function
        while True:
            if(scanner+1 < len(wordList) and
               wordList[scanner+1] != ")" and
               scanner+2 < len(wordList)):
                scanner += 1
                pass
            elif(scanner+1 >= len(wordList)):
                scanner = -1
                break
            # when the closing bracket has been found
            else:
                scanner += 1
                break

        # if there is a closing bracket, we now evaluate it the contents inside of the bracket are
        # valid params or not
        if (scanner != -1):
            i_index = anchor
            i_count = 0
            i_valid = True
            while i_index < scanner:
                if(i_count % 2 == 1 and wordList[i_index] != ","):
                    i_valid = False
                    break
                i_index += 1
        else:
            i_valid = False

        if(i_valid):
            annotateList.append(x + ('B-API', ))
            # tag everything here
            for i in range(anchor+1, scanner):
                #print(i)
                pos_i = posTagList[i]
                annotateList.append(pos_i + ('I-API', ))

            annotateList.append(posTagList[scanner] + ('L-API', ))
            # shift index to scanner + 1
            index = scanner + 1

        # skip the next line
        pass
        
    
    # if not related, append O
    annotateList.append(x + tag)

    index += 1

# print(annotateList)
print("done")

with open("annotation.txt", "wb") as myfile:
    for x in annotateList:
        string = x[0] + " " + x[1] + " " + x[2] + "\n"
        myfile.write(string.encode('utf8'))
