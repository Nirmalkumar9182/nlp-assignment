import operator

with open("answer_without_angle.txt", encoding='utf-8') as file:
    content1 = file.readlines()
with open("question_without_angle.txt", encoding='utf-8') as file:
    content2 = file.readlines()

content = content1 + content2
totalList = []
totalSet = set()
wordDict = dict()
stopWords = ["a", "and", "the"]

for line in content:
    s = line.split()
    totalList = totalList + s
#print("totalList = ", end="")
#print(totalList)

for word in totalList:
    totalSet.add(word)
#print("totalSet = ", end="")
#print(totalSet)

for uniqueWord in totalSet:
    uniqueWordCount = totalList.count(uniqueWord)
    if (uniqueWord not in stopWords):
        wordDict[uniqueWord] = uniqueWordCount

sorted_wordDict = sorted(wordDict.items(), key = operator.itemgetter(1), reverse=True)
for value in sorted_wordDict:
    print (value)