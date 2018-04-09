
class Digit_Data_IO:

    def __init__(self, fl):
        self.img = [[0 for x in range(32)] for y in range(32)]
        self.answer = 0
        self.idx = 0
        self.file = open(fl,'r')
        self.done = False



    def readNextNum(self):
        self.file.seek(self.idx)
        for i in range(32):
            next = self.file.readline()
            if next == '':
                self.done = True
                #print("DONE READING FILE")
                self.idx = 0
                return
            for j in range(len(next) - 1):
                self.img[i][j] = int(next[j])

        self.answer = int(self.file.readline()[1])
        self.idx = self.file.tell()

