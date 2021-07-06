class ValueCalculator:
    def __init__(self,val:str):
        self.val=val
    def __add__(self,other):
        return self.val+other.val
class A:
    pass

if __name__=="__main__":
    print('hi')
