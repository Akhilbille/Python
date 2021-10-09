class Cartoon:
    def __init__(self, cartoon_name, rating):
        self.cartoon_name = cartoon_name
        self.rating = rating

    def details(self):
        print(f"Cartoon Name is {self.cartoon_name} \n and Rating is {self.rating}")


tom_and_jerry = Cartoon("Tom and jerry", 10)
ben10 = Cartoon("Ben10", 10)
print(tom_and_jerry.cartoon_name)
print(tom_and_jerry.rating)
