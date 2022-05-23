# BY gaurav nv
# Write a Python Program for t-test for the following problems and compute the result.
# 1. A random sample of 10 boys had the following IQ’s: 70, 120, 110, 101, 88, 83, 95, 98, 107 &
# 100. Does the data support the assumption of a population mean IQ of 100?

class TestHypo:
    def __init__(self,pop_mean,s,n):
        self.pop_mean = pop_mean
        self.s = s
        self.n = n
        self.avg = 0.0
        
    def CalcAvg(self):
        self.avg = self.s/self.n
    
    def tellResult(self):
        if self.avg == self.pop_mean:
            print("the assumption of a population mean "+ str(self.pop_mean) + " Correct")
    
        else:
            print("the assumption of a population mean "+ str(self.pop_mean) + " is wrong.")

ls = [70,120,110,88,83,95,98,107,100]
t = TestHypo(100,sum(ls),len(ls))
t.CalcAvg()
t.tellResult()

# o/p the assumption of a population mean 100 is wrong.



