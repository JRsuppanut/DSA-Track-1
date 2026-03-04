import heapq
import csv

class Course:
    def __init__(self , code , name , type , credit  , semester , lecturer):
        self.code = code
        self.name = name
        self.type = type
        self.credit = credit
        self.semester = semester
        self.lecturer = lecturer

        self.undo.activate = True

    def __str__(self):
        return f"{self.code} | {self.name} | {self.type} | {self.credit} | {self.semester} | {self.lecturer}"
    

