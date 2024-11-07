class house:
    window=4
    doors=0
    def colors(self,doors):
        self.doors=doors
        print(self.doors)
   
house1=house()
house2=house()
print(house1)
house1.doors=7
print(house1.doors)
house1.colors(10)