from random import random
from student import*

class group(object):
 def __init__(self,student_list):
  self.student_list = student_list
  i = 0
  for stud in student_list:
   i += 1
   stud.set_id(i)

 def __str__(self):
  for stud in student:
   print stud

 def add_student(self,student):
  self.student_list.extend(student)

 def remove_student(self,student_id):
  slist = self.student_list
  slistl = self.student_list[:,student_id]
  slistu = self.student_list[student_id,:]
  self.student_list = slistl.extend(slistu)
  for stud in student_list:
   i += 1
   stud.set_id(i)

 def check_attendance(self):
  for stud in self.student_list:
   stud.check_attendace(random<0.8)

 def add_grade(self,stud_id,grade):
  self.student_list[stud_id].add_grade(grade)

# def avg_grade_class(self):
#  
#  for stud in self.student_list:
#
# def avg_attendance_class(self):

if __name__ == "__main__":
 studl = [student("Marian","Mariamski"), student("Marian","Marianowicz"), student("Marian", "Marianiak")]
 gr = group(studl)
 #print gr

 gr.check_attendance()
 gr.check_attendance()
 gr.check_attendance()
 gr.check_attendance()
 gr.check_attendance()
 gr.check_attendance()
 gr.check_attendance()

print (studl[2].grades)
print gr
