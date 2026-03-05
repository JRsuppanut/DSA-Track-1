import csv
import heapq

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
        return f"{self.code:<10} | {self.name:<75} | {self.c_type:<5} | {self.credit:<8} | {self.semester:<3} | {self.lecturer}"
    __repr__ = __str__

class RegisterSysyem:
    def __init__(self , loaded_courses):
        self.all_courses = loaded_courses
        # Create Dict for the course
        self.course_dict =  {}
        for i in loaded_courses:
            if i.code not in self.course_dict:
                self.course_dict[i.code] = []
            self.course_dict[i.code].append(i)

        self.priority_queue = []
        self.history_stack = []


    def add_course(self , course_code):
        # check if not found the course code
        if course_code not in self.course_dict:
            print(f"❌ not found {course_code} in system")
            return
        
        # a box contain all sections of this course  
        available_section = self.course_dict[course_code] 

        # Select section system
        if len(available_section) == 1:
            selected_course = available_section[0]
        else:
            print(f"    {course_code} {available_section[0].name} have many sections. Please select the section:")
            i = 1
            for course in available_section:
                print(f"type [{i}] to {course.lecturer:<3} - {course.c_type}")
                i += 1

            while True:
                try:
                    choice = int(input(f"select 1-{len(available_section)} : "))
                    if 1 <= choice <= len(available_section):
                        selected_course = available_section[choice - 1]
                        break
                    else:
                        print("❌ Invalid number, try again.")
                except:
                    print("❌ Please, Type a number")

        self.history_stack.append(selected_course)

        priority = 1 if selected_course.c_type == 'Sec' else 2
        heapq.heappush(self.priority_queue, (priority, selected_course.code, id(selected_course), selected_course))
        
        print(f"✅ added : {selected_course.code} {selected_course.name} ({selected_course.c_type} - {selected_course.lecturer})\n")
    
    def undo(self):
        pass

    def process_all(self):
        pass 

    def print_all_course(self):
        print(f"\n---------Show all courses {len(self.all_courses)} courses---------")
        for course in self.all_courses:
            print(course)
        print("")

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

def main():
    #---------system process-----------
    myCourse = loadCourse('CprE_Subject.csv')
    regis_system = RegisterSysyem(myCourse)
    regis_system.print_all_course()

    #---------user process------------
    #test
    regis_system.add_course('010123219')
    regis_system.add_course('010113139')

main()
