For dataset analysis, 3 python scripts were used, any Python IDE like IDLE or pyCharm can be used to run them. It is important to make sure that output.xml is in the same directory as the scripts, otherwise the file path has to be specified when ouput.xml is opened.

"QuestionAnswerCounter.py"
This script counts the amount of question posts and answer posts in output.xml.

The relevant attribute for this task is "PostTypeId". An ID of 1 indicates that the post is a question, and an ID of 2 indicates that the post is an answer. Simply run the script and the counts will be returned.


"AnswerDistribution.py"
This script gives the amount of question posts with x answers in output.xml, where x starts from 0 and increments until equal to the answer count of the post with the most answers.

The relevant attribute for this task is "AnswerCount". The script counts the amount of posts with "AnswerCount=x", lists the number, and then increments x and repeats. After running the script the distribution will be returned. The numbers were then copied into an excel spreadsheet "Data Collection.xlsx" and a simple function was used to obtain the percentages.

"PostLengthDistribution.py"

This script gives the amount of posts that have a word count within a certain range in output.xml, and displays all the ranges. The ranges start from 0 - 50, and keep incrementing by 50 until the longest post has been assigned to a range.

Upon running the script there is an option to include the titles of question posts in the count, press 'Y' to include them or 'N' not to, then press enter.

The Python split() method is used to split each post into a list of words, the length of the list is then taken as the length of that particular post, and appended to another list. At the end, this other list will contain the lengths of all posts. It is then sorted and lengths within each range are categorized accordingly to produce the distribution.

The numbers were then copied into an excel spreadsheet "Data Collection.xlsx" and a simple function was used to obtain the percentages.


