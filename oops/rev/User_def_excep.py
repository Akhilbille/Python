class InvalidException(Exception):
    pass
class LessMarksException(Exception):
    pass
class Student:
    def __init__(self,stu_id,marks):
        self.__stu_id=stu_id
        self.__marks=marks
    def award_schorlarship(self):
        try:
            if (not self.__stud_id.startswith("A")):
                raise InvalidException("Student Id is wrong")
            if (self.__marks<85):
                raise LessMarksException("Studdent has scored less marks")
            print("Student is awarded with scholarship")
        except InvalidException as e:
            print(e)
        finally:
            print("Inside Finally")
try:
    student=Student("B110",84)
    student.award_schorlarship()
except InvalidException as e:
    print(e)
except LessMarksException as e:
    print(e)
finally:
    print("Out side finally")
