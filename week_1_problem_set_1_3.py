myWords = ['zykzexlhdmebqpjf', 'hivdxccsu', 'hpsosdmbhadgixrt', 'mawewbkdhgnevnaccz', 'azcbobobegghakl', 'dagmznlqwwgeb']
answer = ['kz' , 'ccsu', 'adgix', 'accz', 'beggh', 'agmz']

for i in range(len(myWords)):
    s = myWords[i]
    myStr = ""
    tempStr = ""
    for letter in s:
        if tempStr == "":
            tempStr += letter
        else:
            tempLtr = tempStr[-1]
            if tempLtr <= letter:
                tempStr += letter
            else:
                if myStr == "" or len(tempStr) > len(myStr):
                    myStr = tempStr
                    tempStr = letter

    print("Longest substring in alphabetical order is: " + myStr + " = " + str(myStr == answer[i]))
