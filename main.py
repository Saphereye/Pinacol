class FileCompression:
    def __init__(self, text):
        self.debugFile = open('Debug.txt', 'w')
        self.outputFile = open('OutputFile.das', 'w')
        self.secretFile = open('Secret.das', 'w')
        self.textList = text.split(' ')
        for i in self.textList:
            if i == '':
                self.textList.remove(i)
        self.debugFile.write(f"Input List:{self.textList}\n")
        self.keys = {}
        self.wordFrequency = []
        self.output = ''
        self.encodingList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                             '_', '-', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')',
                             '{', '}', '[', ']', ',', '/', '+', ':', ';', "'", "`", "~",
                             '?', '<', '>']

    def DebugFileClose(self):
        self.debugFile.close()

    def CreateSecret(self):
        outputString = str(self.wordFrequency)
        outputString = outputString.replace(' ', '')
        outputString = outputString.replace(',', ' ')
        outputString = outputString.replace("'", '')
        outputString = outputString.replace('[', '')
        outputString = outputString.replace(']', '')
        self.secretFile.write(outputString)

    def Encoder(self, indexNumber):
        output = ''
        while indexNumber:
            if indexNumber < len(self.encodingList)+1:
                output += self.encodingList[indexNumber - 1]
                break
            else:
                output += self.encodingList[(indexNumber % len(self.encodingList))-1]
                indexNumber //= len(self.encodingList)
        output = output[::-1]
        self.debugFile.write(f"Encoded output : {output}\n")
        return output

    def CreateKeys(self):
        for i in self.textList:
            try:
                self.keys[i] += 1
            except KeyError:
                self.keys[i] = 1
        self.debugFile.write(f"Frequency Key dictionary:{self.keys}\n")

    def OrderByFrequency(self):
        self.wordFrequency = [i for i in self.keys]
        self.wordFrequency.sort(key=(lambda key: self.keys[key]), reverse=True)
        self.debugFile.write(f"Order by Frequency:{self.wordFrequency}\n")

    def FinalEncode(self):
        outputString = ''
        self.CreateKeys()
        self.OrderByFrequency()
        for i in self.textList:
            temporaryVariable = self.Encoder(self.wordFrequency.index(i))
            outputString += temporaryVariable+'.' if len(temporaryVariable) != 1 else temporaryVariable
        self.DebugFileClose()
        self.outputFile.write(outputString)
        self.CreateSecret()
        return outputString


if __name__ == "__main__":
    inputFile = open('InputFile.txt', 'r')
    inputString = inputFile.read()
    trial = FileCompression(inputString)
    print(trial.FinalEncode())
