class Humanbeing:
    hands = 2
    legs = 2

    @classmethod
    def info(cls, name):
        print(f"{name} has {cls.legs}legs and has {cls.hands}hands ")


Humanbeing.info("kiran")
Humanbeing.info("Akhil")
