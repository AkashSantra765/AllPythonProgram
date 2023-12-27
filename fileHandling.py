#test 1
'''f=open('test1.txt','w')
f.close'''

#another way test 1
'''with open('text1.txt','w') as f:
    f.write("Be agood listner")'''

    #another way test 2 using function
'''def writing(file,text):
    with open(file,'w') as f:
        f.write(text)
writing('text2.txt','Lets crack JECA 2023')'''

#Test 3 open with append
'''def append(file,text):
    with open(file,'a') as f:
        f.write(text)
append('text3.txt','\nLets crack JECA 2023 and you are ready for 2024')
'''

#Read the data test 3
'''def reading(file):
    with open(file,'r') as f:
        text=f.read()
        print(text)
reading('text3.txt')'''


              #Searching 

def searching(file,word):
    try:
        with open(file,'r') as f:
            f.read()
            lineCount=0
            for i in f.readlines():
                lineCount+=1
                wordList=i.split(' ')
                wordCount=0
                for j in wordList:
                    wordCount+=1
                    if word==j:
                        return(lineCount,wordCount)
            else:
                return None
    except FileNotFoundError:
        print("word is not found")
searching('text3.txt','JECA')











