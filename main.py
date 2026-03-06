import csv
import heapq

class Course:
    def __init__(self , code , name , c_type , credit  , semester , lecturer):
        self.code = code
        self.name = name
        self.c_type = c_type
        self.credit = credit[0]
        self.semester = semester
        self.lecturer = lecturer

        self.isActivate = True

    def __str__(self):
        return f"{self.code:<10} | {self.name:<75} | {self.c_type:<5} | {self.credit:<7} | {self.semester:<8} | {self.lecturer}"
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
            print(f"{course_code} {available_section[0].name} have many sections. Please select the section:")
            i = 1
            for course in available_section:
                print(f"     type [{i}] to {course.lecturer:<3} - {course.c_type}")
                i += 1

            while True:
                try:
                    choice = int(input(f"     select 1-{len(available_section)} : "))
                    if 1 <= choice <= len(available_section):
                        selected_course = available_section[choice - 1]
                        break
                    else: # case input is over length
                        print("❌ Invalid number, try again.")
                except: # case input is not number
                    print("❌ Please, Type a number")

        selected_course.isActivate = True
        self.history_stack.append(selected_course)

        # Keep only the last 3 actions (so undo works only for the last 3 adds)
        if len(self.history_stack) > 3:
            self.history_stack.pop(0)

        priority = 1 if selected_course.c_type == 'Sec' else 2
        heapq.heappush(self.priority_queue, (priority, selected_course.code, id(selected_course), selected_course))
        
        print(f"\n✅ added : {selected_course.name} ( {selected_course.credit} ) to {selected_course.lecturer} ( {selected_course.c_type} )) \n")
    
    def undo(self):
        # Undo is possible only if we still have history
        if len(self.history_stack) == 0:
            print("Nothing to undo.\n")
            return

        # Get the most recently added course (LIFO)
        course = self.history_stack.pop()

        # Mark it inactive (lazy delete).
        # We do NOT remove it from the heap because heapq does not support efficient removal.
        course.isActivate = False

        print(f"🔃 REVERTED: {course.name} removed from {course.lecturer}.\n")

    def process_all(self):
        print("-----------✅ Register is Completed ✅-----------")
        if not self.priority_queue:
            print("not available course in queue \n") 
            return

        course_amount = 0
        total_course_cradit = 0

        while self.priority_queue:
            priority, code, course_id, course = heapq.heappop(self.priority_queue)

            if course.isActivate :
                course_amount += 1
                total_course_cradit += int(course.credit)

                print(f"[{course.c_type:^5}] {course.code:<10} | {course.name:<45} | ผู้สอน: {course.lecturer}")
        
        print("-" * 75)
        print(f"รวมจำนวนวิชาที่ลงทะเบียน: {course_amount} วิชา")
        print(f"รวมหน่วยกิตทั้งหมด: {total_course_cradit} หน่วยกิต")
        print("=========================================\n")

    def print_all_course(self):
        print(f"\n-----------Show all courses {len(self.all_courses)} courses-----------")
        print(f"{"Code":<10} | {"Name":<75} | {"Type":<5} | {"Credits":<5} | {"Semester":<5} | {"Lecturer"}")
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
    print("-----------start Register-----------")
    
    
    # regis_system.add_course('010123219')
    # regis_system.add_course('010113139')
    # regis_system.undo()
    # regis_system.process_all()

main()