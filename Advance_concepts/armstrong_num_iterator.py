class ArmstrongIter:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<0:
            raise StopIteration
        else:
            
            while True:
                length=len(str(self.num))
                num=self.num
                arms=0
                while num!=0:
                    last_digit=num%10
                    arms+=last_digit**length
                    num//=10
                
                if self.num==arms:
                        val=self.num
                        self.num+=1
                        return val
                self.num+=1
arms1=ArmstrongIter()   
print(next(arms1))   
print(next(arms1))   
print(next(arms1))   
print(next(arms1))   
print(next(arms1))   
print(next(arms1)) 
print(next(arms1))   

print(next(arms1))   

print(next(arms1))   
print(next(arms1))   
print(next(arms1))   
print(next(arms1))   

  


            

            


