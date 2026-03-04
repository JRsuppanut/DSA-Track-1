import csv

class Course:
    def __init__(self , code , name , c_type , credit  , semester , lecturer):
        self.code = code
        self.name = name
        self.c_type = c_type
        self.credit = credit
        self.semester = semester
        self.lecturer = lecturer

        self.isActivate = True

    def __str__(self):
        return f"{self.code:<10} | {self.name:<35} | {self.c_type:<5} | {self.credit:<8} | {self.semester:<3} | {self.lecturer}"
    __repr__ = __str__

def loadCourse(filename):
    allCourse = []
    with open(filename , mode='r', encoding='utf-8-sig' ) as file:
        reader = csv.reader(file)
        next(reader) #skip the 1st line (it's not data)

        for row in reader:
            course_object = Course(
                code=row[0].strip(),
                name=row[1].strip(),
                c_type=row[2].strip(),
                credit=row[3].strip(),
                semester=row[4].strip(),
                lecturer=row[5].strip())

            allCourse.append(course_object)
    
    return allCourse


myCourse = loadCourse('CprE_Subject.csv')
print(f"length : {len(myCourse)}")
print(*myCourse[:5], sep='\n')
