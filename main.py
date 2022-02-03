class FileCompression:
    def __init__(self, text: str):
        self.inputLength = len(text)
        self.outputLength = 0
        self.keyLength = 0
        self.debugFile = open('Debug.txt', 'w')
        self.outputFile = open('OutputFile.das', 'w')
        self.secretFile = open('Secret.das', 'w')

        # Separating input by ' ', and converting it into a list
        self.textList = text.split(' ')

        # Removing any empty strings
        for i in self.textList:
            if i == '':
                self.textList.remove(i)

        # Writing the word list into the debug file
        self.debugFile.write(f"Input List:{self.textList}\n")
        self.keys = {}
        self.wordFrequency = []
        self.output = ''

        # Key by which the encoding will take place
        self.encodingList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                             '_', '-', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')',
                             '{', '}', '[', ']', ',', '/', '+', ':', ';', "'", "`", "~",
                             '?', '<', '>']

        # Less elements for testing purposes
        # self.encodingList = ['0', '1']

    def CreateSecret(self):
        # Create the code by which encoding takes place
        outputString = str(self.wordFrequency)
        outputString = outputString.replace(' ', '')
        outputString = outputString.replace(',', ' ')
        outputString = outputString.replace("'", '')
        outputString = outputString.replace('[', '')
        outputString = outputString.replace(']', '')
        self.secretFile.write(outputString)
        self.secretFile.close()
        self.keyLength = len(outputString)

    def Encoder(self, indexNumber: int) -> str:
        # encoding each element one at a time
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
        # Frequency distribution dictionary is created
        # Dictionary helps in speeding up element call process
        # When sorting the word list on basis on frequency
        for i in self.textList:
            try:
                self.keys[i] += 1
            except KeyError:
                self.keys[i] = 1
        self.debugFile.write(f"Frequency Key dictionary:{self.keys}\n")

    def OrderByFrequency(self):
        # Creating list based on frequency
        # Helps giving least length elements to
        # words occurring most
        self.wordFrequency = [i for i in self.keys]
        self.wordFrequency.sort(key=(lambda key: self.keys[key]), reverse=True)
        self.debugFile.write(f"Order by Frequency:{self.wordFrequency}\n")

    def FinalEncode(self) -> str:
        # Joining all element to make final string
        outputString = ''
        self.CreateKeys()
        self.OrderByFrequency()
        for i in self.textList:
            temporaryVariable = self.Encoder(self.wordFrequency.index(i))
            outputString += temporaryVariable + '.' if len(temporaryVariable) != 1 else temporaryVariable
        # Close Debug file as not needed for any more operations
        self.debugFile.close()

        # Write the output in OutputFile.das
        self.outputFile.write(outputString)
        self.outputFile.close()

        # Write the secret code in Secret.das
        self.CreateSecret()

        # Recording length of output to check compression ration
        self.outputLength = len(outputString)

        return outputString

    def CompressionRatio(self) -> str:
        # Uncompressed Size / Compressed Size, value greater than 1 is good, less than 1 is a loss
        return f"Compression Ratio = {(self.inputLength / (self.keyLength + self.outputLength))}"

    def CompressingPercent(self) -> str:
        # Size% of compressed file relative to input file
        return f"Output file is {(self.outputLength/self.inputLength) * 100} % of input file."


if __name__ == "__main__":
    with open('InputFile.txt', 'r') as inputFile:
        inputString = inputFile.read()
    trial = FileCompression(inputString)
    trial.FinalEncode()
    print(trial.CompressionRatio())
    print(trial.CompressingPercent())
