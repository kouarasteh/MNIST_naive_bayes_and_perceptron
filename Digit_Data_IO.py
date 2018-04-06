
class Digit_Data_IO:

    def __init__(self, fl):
        self.img = [[0 for x in range(32)] for y in range(32)]
        self.answer = 9
        self.idx = 0
        self.file = open(fl,'r')





    def readNextNum(self):
        print('seeking :',self.idx)
        self.file.seek(self.idx)
        for i in range(32):
            self.img[i] = self.file.readline()

        self.answer = int(self.file.readline()[1])
        self.idx = self.file.tell()

        for i in range(32):
            print(self.img[i],end='')

        print("above is a:", self.answer)


dd = Digit_Data_IO('digitdata/optdigits-orig_train.txt')
dd.readNextNum()
dd.readNextNum()
dd.readNextNum()
dd.readNextNum()
dd.readNextNum()
dd.readNextNum()
dd.readNextNum()
dd.readNextNum()
