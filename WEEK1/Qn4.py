import random
class TextGenerator:
    def __init__(self):
        self.prefixDict = {}
        self.tuple = {}
        self.words = []
    
    def assimilateString(self,string):
        words = string.split()
        self.words = words
        for i,word in enumerate(words):
            if i+2>= len(words):
                break

            if (words[i],words[i+1]) in self.prefixDict.keys():
                self.prefixDict[(words[i],words[i+1])].append(words[i+2])
            else:
                self.prefixDict[(words[i],words[i+1])] = [(words[i+2])]

            if words[i] in self.tuple.keys():
                self.tuple[words[i]].append(words[i+1])
            else:
                self.tuple[words[i]] = [words[i+1]]


    def assimilateText(self,fileName):
        f = open(fileName , 'r')
        fstring = f.read()
        self.assimilateString(fstring)
        f.close()
        return 
    
    def generateText(self,length,startWord = None):
        if length<0:
            return ""
        
        if startWord == None :
            startWord = random.choice(self.words)
        elif startWord not in self.words:
            raise Exception("Unable to produce text with the specified start word")
        
        if length == 1:
            return startWord
        sentence = [startWord]
        sentence.append(self.findNextWord(startWord))

        for i in range(length-2):
            sentence.append(self.findNextWord(sentence[-2],sentence[-1]))

        print(" ".join(sentence))

    def findNextWord(self,firstWord,secondWord= None):
        if secondWord == None:
            try:
                return random.choice(self.tuple[firstWord])
            except:
                return random.choice(self.words)
        
        try:
            return random.choice(self.prefixDict[(firstWord,secondWord)])
        except:
            try:
                return random.choice(self.tuple[firstWord])
            except:
                return random.choice(self.words)
            
if __name__ == "__main__":
    t = TextGenerator()
    t.assimilateText('Sherlock.txt')
    t.generateText(100)