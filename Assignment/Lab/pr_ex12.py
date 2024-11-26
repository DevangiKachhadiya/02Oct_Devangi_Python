'''Write a Python program to demonstrate the use of local and
global variables in a class.'''

G="This Is Global Variable"

class KD:
    def data(self):
        L="This Is Local Variable"
        print(L)
        print(G)

kd=KD()
kd.data()
