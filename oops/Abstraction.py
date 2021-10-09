class Abstract:
    def __init__(self):
        self.__private = "Personal information"

    def get_private(self):
        return self.__private


obj = Abstract()

print(obj._Abstract__private)
"""obj.set_private("Some personal matter")
print(obj.get_private())
obj.set_private("New personal Information")
print(obj.get_private())"""
