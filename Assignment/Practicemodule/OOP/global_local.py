#global Variable
A=100
B=500

class Math:
    def Production(self):
        #Local Variable
        a=50
        b=2
        print(f"Mul: {a*b} ->This Is Local Variable")

m=Math()
m.Production()
print(f"Sum: {A+B} ->This Is Global Variable ")
