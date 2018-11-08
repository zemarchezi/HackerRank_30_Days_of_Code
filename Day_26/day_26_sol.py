class ReturnFine:
    def __init__(self,dateRet, dateExp):
        self.dayR = int(dateRet[0])
        self.monthR = int(dateRet[1])
        self.yearR = int(dateRet[2])

        self.dayE = int(dateExp[0])
        self.monthE = int(dateExp[1])
        self.yearE = int(dateExp[2])
    def returnFine(self):
        fee = 0
        if self.yearR > self.yearE:
            fee = 10000
        elif self.yearE == self.yearR:
            if self.monthR > self.monthE:
                fee = (self.monthR - self.monthE) * 500
            elif self.monthR == self.monthE and self.dayR > self.dayE:
                fee = (self.dayR - self.dayE) * 15

        return (fee)

actualyRet = input()
expectedRet = input()

rt = ReturnFine(actualyRet.split(' '),expectedRet.rsplit(' '))
print (rt.returnFine())
