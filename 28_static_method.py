class School:
    school_name="Shanzid High School"
#no object need for static method.
    @staticmethod #have to use this for staic method.
    def show_grade(grade):
        if grade>=90:
            print("A+")
        elif grade<90 and grade>=85:
            print("A")
        else:
            print("F")
School.show_grade(90)
o1=School
o1.show_grade(50)
        