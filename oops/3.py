class Methods_prac:
    def __init__(self):
        self.__lucky_num = 10

    def get_lucky_num(self):
        return self.__lucky_num

    def set_lucky_num(self, new_num):
        self.__lucky_num = new_num


obj1 = Methods_prac()
print(obj1.get_lucky_num())
