class School:
    school_name = "Ostad High School"
    def __init__(self, name):
        self.student_name = name
    
sc1 = School("Rahim")
scl2 = School("Karim")
print(sc1.school_name)
print(sc1.student_name)
print(scl2.school_name , scl2.student_name)
