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

        self.isActivate = False

    def __str__(self):
        return f"{self.code:<10} | {self.name:<75} | {self.c_type:<5} | {self.credit:<7} | {self.semester:<8} | {self.lecturer}"
    __repr__ = __str__


class RegisterSystem:
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

        for i in available_section:
            if i.isActivate :
                print(f"⚠️ You have already registered for {course_code}\n")
                return

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
                    choice = int(input(f"     select [1] - [{len(available_section)}] : "))
                    if 1 <= choice <= len(available_section):
                        selected_course = available_section[choice - 1]
                        break
                    else: # case input is over length
                        print("❌ Invalid number, try again.")
                except ValueError: # case input is not number
                    print("❌ Please, Type a number")

        selected_course.isActivate = True
        self.history_stack.append(selected_course)


        priority = 1 if selected_course.c_type == 'Sec' else 2
        heapq.heappush(self.priority_queue, (priority, selected_course.code, id(selected_course), selected_course))
        
        print(f"✅ added : {selected_course.name} ({selected_course.credit} credits) to {selected_course.lecturer} \n")
    
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
        #credits

        course_amount = 0
        total_course_credits = 0

        while self.priority_queue:
            priority, code, course_id, course = heapq.heappop(self.priority_queue)

            if course.isActivate :
                course_amount += 1
                total_course_credits += int(course.credit)
                
                print(f"[{course.c_type:^5}] {course.code:<10} | {course.name:<45} | Lecturer : {course.lecturer}")
        
        print("-------------------------------------------------------------------------------")
        print(f"Total courses registered : {course_amount} courses")
        print(f"Total credits : {total_course_credits} credits")
        print("*======================================================*\n")

    def print_all_course(self):
        print(f"\n-----------Show all courses {len(self.all_courses)} courses-----------")
        print(f"{'Code':<10} | {'Name':<75} | {'Type':<5} | {'Credits':<5} | {'Semester':<5} | {'Lecturer'}")
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
    regis_system = RegisterSystem(myCourse)
    regis_system.print_all_course()

    #---------user process------------
    #test
    print("-----------start Register-----------")

    while True:
        user_input = input("\n >> ").strip().lower()

        # case user Enter with no input
        if not user_input:
            continue
        # get userinput first block to cammand
        command = user_input[0]

        if command == 'add':
            pass

        elif command == 'redo':
            pass
            
        elif command == 'process_all':
            pass

        elif command == 'exit':
            pass
        
        elif command == 'help':
            pass

        else:
            "command not found, Type 'help' to..."
            continue
    # while True:   
    #     try:
    #         print("     Type [1] to add a course")
    #         print("     Type [2] to undo")
    #         print("     Type [3] to confirm")
    #         print("     Type [4] to close program")
    #         UserType = input("     select [1] - [4] : ").strip()
    #         if UserType == '1':
    #             input_code = input("add : ").strip()
    #             regis_system.add_course(input_code)
    #         elif UserType == '2':
    #             regis_system.undo()
    #         elif UserType == '3':
    #             regis_system.process_all()
    #             break
    #         elif UserType == '4':
    #             break
    #         else:
    #             print("❌ Invalid number, try again.")
    #     except ValueError:
    #         print("❌ Please, Type a number")
        

main()