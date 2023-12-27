def searching(file,word):
    try:
        with open(file,'r') as f:
            f.read()
            lineCount=0
            for i in f.readlines():
                lineCount=+1
                wordList=i.split(' ')
                wordCount=0
                for j in wordList:
                    wordCount=+1
                    if word==j:
                        return(lineCount,wordCount)
            else:
                return None
    except FileNotFoundError:
        print("word is not found")
