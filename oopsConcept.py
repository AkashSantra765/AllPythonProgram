class student:
    school="Andichak"

    def __init__(self):
        self.marks=10
    
    def get_marks(self):
        return self.marks
    
    @classmethod
    def get_school(cls):
        return cls.school
    
    @staticmethod
    def add(x,y):
        return x+y
    
s1=student()
print(s1.get_marks())
print(student.get_school())
print(s1.add(3,4))