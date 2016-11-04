# CZ4045 NLP Assignment Readme
4th November 2016

The following libraries are used in this project:
* [Apache Commons Compress](http://commons.apache.org/proper/commons-compress/index.html)
* [XZ for Java (Maven)](http://tukaani.org/xz/java.html)
* [Natural Language Toolkit (NLTK)](http://www.nltk.org/)
* [BRAT Annotation Tool](http://brat.nlplab.org/)

The following IDEs have been used to run the programs created for this project:
* [IntelliJ IDEA](https://www.jetbrains.com/idea/)
* [Eclipse](http://www.eclipse.org)
* [IDLE 3.5.2](https://www.python.org/downloads/)
* [Visual Studio 2015 Community](https://www.visualstudio.com/downloads/)

Our team's project revolves around the output.xml file which was generated from the 7z archive:

1. The project uses the dataset downloaded from https://archive.org/details/stackexchange. The particular file used was https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z (sized 9.2GB as of current date)
2. The file which was used for analysing statistics for more than 500 posts can be found at https://github.com/shouxian92/nlp-assignment/blob/master/output%20files/others/output.xml
3. The files which were used for annotations can be found in the following folder:
    1. https://github.com/shouxian92/nlp-assignment/blob/master/output%20files/for%20brat
4. The files which were used for k-fold validations can be found in the following folder:
    1. https://github.com/shouxian92/nlp-assignment/tree/master/CRF/Folds

Due of the immense number of individual programs created for the sake of this project. It is highly recommended to view this readme using a markdown viewer like http://dillinger.io/ or can be viewed directly online at our team's git https://github.com/shouxian92/nlp-assignment. However, reading it in a text editor is still very much welcome.

# 7-Zip extractor
A Java program was written by our team to read files compressed in a .7z format. The program is located inside of the '7zip extractor' folder.

This program was coded using IntelliJ IDEA, it is recommended to only be opened with IntelliJ IDEA. The reason why IntelliJ was used in particular for this program is because of how easy IntelliJ can be used to add Maven libraries into a Java project.

There are several libraries which are essential to run the project:

1. All JAR files in the '7zip extractor/lib' folder which contains the Apache Commons Compress essentials
2. 'XZ for Java' to be added as a Maven library under the project (org.tukaani.xz:1.5)

If all libraries are present, the Main java class should be able to execute without any errors. The program will prompt for a location which you have stored the relevant 7z file inside of your computer. If the path is correct, it should extract the relevant XML file into an output file named as output.xml in the root folder of the project.

Note that this program will only run for 2 seconds because the 7z file which was used for this project is too big to complete the actual output processing. This will also mean that the file generated (output.xml) is not a complete XML file, so any incomplete information like broken XML tags at the end of the file should be expected and to be removed. A <rows> tag should be added to the end of the file.

# Porter's Stemming
In order to observe stemming of words from our output file. Our team has used the Porter's Stemming library for Java. The program can be found under 'java/PortersSemming'

# POS Tagging
The POS tag set which was used in this project was the Maxent Treebank POS tag set. To observe how the tagging works, a Java program has been written to first tokenize a string, followed by the tagging of tokens. The POS Tagger can be found under 'java/POSTagger'

# Question-Answer splitter
The question-answer splitter is a Python program written to separate the question posts from the answer posts from the generated output.xml file. The program is located under 'python/QuestionAnswerSplitter/question-answer-splitter.py'.

Instructions to use this program:

1. Place the file (make sure it is named as output.xml) which was generated from the 7-Zip extractor into the same folder as the program
2. Run the python program
3. 2 files named questions.txt and answers.txt will be generated from the program inside of the same folder

# Data Collection
For dataset analysis, 3 python scripts were used, any Python IDE like IDLE or pyCharm can be used to run them. It is important to make sure that output.xml is in the same directory as the scripts, otherwise the file path has to be specified when ouput.xml is opened.

### QuestionAnswerCounter.py
This script counts the amount of question posts and answer posts in output.xml.

The relevant attribute for this task is "PostTypeId". An ID of 1 indicates that the post is a question, and an ID of 2 indicates that the post is an answer. Simply run the script and the counts will be returned.

### AnswerDistribution.py
This script gives the amount of question posts with x answers in output.xml, where x starts from 0 and increments until equal to the answer count of the post with the most answers.

The relevant attribute for this task is "AnswerCount". The script counts the amount of posts with "AnswerCount=x", lists the number, and then increments x and repeats. After running the script the distribution will be returned. The numbers were then copied into an excel spreadsheet "Data Collection.xlsx" and a simple function was used to obtain the percentages.

### PostLengthDistribution.py

This script gives the amount of posts that have a word count within a certain range in output.xml, and displays all the ranges. The ranges start from 0 - 50, and keep incrementing by 50 until the longest post has been assigned to a range.

Upon running the script there is an option to include the titles of question posts in the count, press 'Y' to include them or 'N' not to, then press enter.

The Python split() method is used to split each post into a list of words, the length of the list is then taken as the length of that particular post, and appended to another list. At the end, this other list will contain the lengths of all posts. It is then sorted and lengths within each range are categorized accordingly to produce the distribution.

The numbers were then copied into an excel spreadsheet "Data Collection.xlsx" and a simple function was used to obtain the percentages.

# 100-Post API mentions extractor
This extractor is a Python program written to filter out 100 posts from the given output.xml file. By applying a regex pattern, we count the number of posts which appears until the counter hits 100. The program is located under 'python/QuestionAnswerSplitter/100-post-api-mention.py'.

Instructions to use this program:

1. Place the file (make sure it is named as output.xml) which was generated from the 7-Zip extractor into the same folder as the program
2. Run the python program
2. 5 files named from set0.txt to set4.txt would be generated in the same folder

# Conditional Random Field
For the purpose of API recognition in our project, a Conditional Random Field implementation in C# known as CRFSharp was used, below is a guide on how to train and test a model using the sample training and testing files provided.

Files and folders included in the CRF folder are as follows:

#### CRFSharpDemoPackage
> The CRF tool obtained from https://github.com/zhongkaifu/CRFSharp under "Releases", the bin folder contains CRFSharpWrapper.dll, used for encoding(training), and CRFSharpConsole.exe, used for decoding(testing). The other files remain unused. 
This library is included because the file size is extremely small (343 KB)

#### CRF_for_NLP
> Contains a C# project created in Visual Studio Community 2015. Inside is Program.cs, which is the code for encoding(training) a CRF model.

#### training.txt
> A sample file used for the encoding(training) process. 
Each line contains one token, then a tab, then the POS tag of the token, then another tab, then the BILOU tag of the token.

#### testing.txt
> A sample file used for the decoding(testing) process.
Each line contains one token, then a tab, then the POS tag of the token, but no BILOU tag.

#### template.NE
> The template file used by the CRF tool for feature generation. Each line in the file is an index followed by a rule string. 
The simplest format for rule string is "%x[y,z]", x is a variable that the result will be assigned to, z can be either 0 for the current token or 1 for its POS tag, and y denotes the position relative to the current token.

> For example, assuming the current token is "cats" in:

    like  VB  O
    cats  NNS O
  
> then %x[0,0] will give "cats", %x[0,1] will give "NNS", and %x[-1,0] will give "like".
The rule strings can be further combined like "%x[-1,1]/%x[0,1]" which will give "VB/NNS"

### Instructions for encoding:
1. Open the C# project CRF_for_NLP in Visual Studio, make sure CRFSharpWrapper.dll is already added as a project reference. 
2. Change the string variables "strTemplateFileName" and "strTrainingCorpus" in Program.cs. These contain the file paths that should point to where template.NE and training.txt are located in the system.
3. Also change the string variable "strEncodedModelFileName", this contains the file path where the model files should be outputted to, and also determines the name of the model files ("ner_model" by default).
4. The other parameters can be left as is.
5. Run Program.cs, a command prompt window should open showing that CRFSharp is encoding a model based on training.txt and template.NE
6. After the encoding process is done. 4 model files should be outputted. Assuming the model files are named "ner_model", then these 4 files will be "ner_model", "ner_model.alpha", "ner_model.feature", and "ner_model.feature.raw_text".
7. The encoding process is finished.

### Instructions for decoding:
1. Open a command prompt window.
2. Chance the current directory to 'x\CRFSharpDemoPackage\bin'. Where x stands for the file path where this folder is located on the system.
3. Run the command "CRFSharpConsole.exe -decode -modelfile y\ner_model -inputfile y\testing.txt -outputfile y\testing_results.txt". Where y stands for the file path where the model files outputted earlier during encoding, and the testing file, are located.
4. Observe that a new file, "testing_results.txt", has been created in the directory pointed to by y.
5. This concludes the decoding process. Note how the result file now has BILOU tags for every token.

# CRF training/test file generator
In order to feed the CRF library a file with the correct format it requires, a Python program was written to generate a file suitable for the CRF library. The program is located under 'python/Annotation + POSTagging/api_annotation_parser.py'.

This program tokenizes strings within a file and performs POS tagging with BILOU notation

Instructions to use this program:

1. Place the 2 files required in the same folder as the program. (Namely, the generated set of text file from the 100-Post extractor and the .ann file which was generated from annotating through BRAT)
2. Run the Python program
3. The program will ask for the file name that you wish to perform the processing on
4. The program will then generate 2 new files using the name which was entered in the previous step with a suffix of _training and _test where the latter will not contain the annotation tags while the former will.

Note that the POS tagger still tags the tokens according to the Maxent Treebank POS Tag set

# CRF validator
In order to test the results of our API recognition module, a Python program was written to display the frequency of false, true positives and negatives scores, along with the precision, recall and F1 scores. The program basically compares the BILOU notation using the test result against the validation set. The program is located under 'python/CRFValidator/validator.py'.

Instructions to use this program:

1. Place a test result file and the validation file in the same folder as the program
2. Run the Python program
3. The program will first ask for the test result file's name
4. The program will then ask for the validation file's name
5. The program will generate the relevant scores pertaining to this file
