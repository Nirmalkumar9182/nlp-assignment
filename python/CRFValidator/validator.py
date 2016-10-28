name = input("Welcome to the validator program. What is the name of your file? (without extension) ")

output = []

with open( name + '.txt', 'r', encoding='utf8') as fp:
    for line in fp:
        if(len(line.split()) > 0):
            output.append(line.split())

name = input("What is the name of the answer file? ")
answer = []

with open( name + '.txt', 'r', encoding='utf8') as fp:
    for line in fp:
        if(len(line.split()) > 0):
            answer.append(line.split())

correct = 0
truePositive = 0;
falsePositive = 0;
trueNegative = 0;
falseNegative = 0;

if(len(answer) == len(output)):
    for i in range(0, len(answer)):
        # False positive: detects as U or BIL when it is supposed to be O
        # True positive: detects as U or BIL when it is
        # False negative: detects as O but it is actually BIL or U
        # True negative: detects as O when it is
        if(len(answer[i]) > 0):
            if(answer[i][2] == output[i][2] and answer[i][2] == "O"):
                trueNegative += 1
            elif(answer[i][2] == output[i][2]):
                truePositive += 1
            else:
                 if(output[i][2] == "O"):
                     falseNegative += 1
                 else:
                     falsePositive += 1
                     
    print("Total number of items: " + str(len(answer)))
    print("Stats:")
    print("True Positive - " + str(truePositive))
    print("False Positive - " + str(falsePositive))
    print("True Negative - " + str(trueNegative))
    print("False Negative - " + str(falseNegative))
    print()
    '''
    Precision = True Positive/ (True Positive + False Positive)
    Recall = True Positive/ (True Positive  + False Negative)
    F1 score = 2 * ((Precision * recall) / (Precision + recall))
    '''
    precision = truePositive / (truePositive + falsePositive)
    recall = truePositive / (truePositive + falseNegative)
    f1 = 2 * ((precision * recall) / (precision + recall))
    print("Precision - " + str(precision))
    print("Recall - " + str(recall))
    print("F1 score - " + str(f1))
    
else:
    print("The output files and answer files are different")
