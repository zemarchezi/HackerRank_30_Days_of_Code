class SplitString:
    def __init__(self,string):
        self.str = string
    def splitString(self):
        lista = list(self.str)
        list_even = list()
        list_odd = list()
        index = 0

        for letter in lista:
            if index % 2 != 0:
                list_even.append(letter)
            else:
                list_odd.append(letter)
            index += 1

        string_even = "".join(list_even)
        string_odd = "".join(list_odd)

        print(string_odd + ' ' + string_even)

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        s = str(input())
        sp = SplitString(s)
        sp.splitString()

            
