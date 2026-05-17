class School:
    school_name="Shanzid High School" #Class variable and it is applicable for all object of this class
    def __init__(self, name):
        self.student_name=name #instance varianle


sc1=School("Shanzid")
print(sc1.student_name)
print(sc1.school_name)
sc2=School("Losmi")
print(sc2.student_name)
print(sc2.school_name)
#Now we will change the class variable for specific object
sc2.school_name="BracU"
print(sc2.student_name)
print(sc2.school_name)
#if we want to change or update class variable
School.school_name="AIUB"
print(sc1.student_name)
print(sc1.school_name)
