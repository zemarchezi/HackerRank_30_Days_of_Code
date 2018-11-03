class PhoneBook:
    def __init__(self, data, inp):
        self.inp = inp
        self.names = data

    def readData(self):
        if self.inp in self.names:
            print(self.inp + "=" + self.names[self.inp])
        else:
            print("Not found")


if __name__ == '__main__':

    n = int(input())

    names = {}

    for i in range(n):
        a, b=input().strip().split()
        names.update({a:b})

    for i in range(n):
        a=input().strip()

        ph = PhoneBook(names, a)
        ph.readData()
