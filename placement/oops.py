class Box:
    def __init__(self,boxid,length,breadth,height):
        self.boxid=boxid
        self.length=length
        self.breadth=breadth
        self.height=height
    def status(self):
        self.status="Available"
    def getVolume(self):
        return self.length*self.breadth*self.height

class ShippingCompany(Box):
    def __init__(self,boxList):
        self.boxList=boxList
    def findBoxesToPack(self,volume):
        self.volume=volume
        for obj in self.boxList:
            if obj.status =="Available" and obj.getVolume<obj.volume:
                obj.status="Packaged"      


    def findBoxToShip(self,capOfACargo):
        self.cap=capOfACargo
        if (self.status=='packaged' and self.volume <self.cap ):
            self.status="Sent"
        else:
             return 0




