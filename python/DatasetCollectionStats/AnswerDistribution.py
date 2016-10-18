import re

with open("output.xml", encoding='utf-8') as file:
    content = file.readlines()

answerCounter = 0
numberOfMatches = 0
total = 0
tempList = []

while total < 263:  #Only 263 questions, can stop once logged answer counts for all of them
    answerCounterString = r'AnswerCount="' + str(answerCounter) + '"'
    for line in content:
        tempList.extend(re.findall(answerCounterString, line)) #check if AnswerCount="x" exists in this particular line
    numberOfMatches = len(tempList)     #gives num of questions that have x answers
    total += len(tempList)              #tracks num of questions in total that have their answer counts logged

    print("Number of questions with " + str(answerCounter) + " answers = " + str(numberOfMatches))
    #preparation for iteration of AnswerCount="x+1"
    answerCounter += 1
    numberOfMatches = 0
    tempList.clear()