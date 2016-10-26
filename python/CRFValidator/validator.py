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

if(len(answer) == len(output)):
    for i in range(0, len(answer)):
        if(len(answer[i]) > 0 and answer[i][2] == output[i][2]):
            correct += 1

    print("Total number of items: " + str(len(answer)) + ", total number of correct items: " + str(correct))
else:
    print("The output files and answer files are different")
