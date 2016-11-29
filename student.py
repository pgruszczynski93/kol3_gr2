#-*- coding: utf-8 -*-

#file contains classes needed for implementing complete highscool diary
from random import randrange

lectures_available = {0:'maths',1:"astrophisics",2:"phisics",3:"history",4:"astrohistory"}

class Student(object):
 def __init__(self,name,surname,lectures_id):
  self.stud_data = {'name':name,'surname':surname,'grades':[[],[],[],[],[]],'attendances':[[],[],[],[],[]]}
  for lecture in lectures_id:
   self.lectures_id = lectures_id

 def print_stud(self,group_id):
  return  self.stud_data['name'] + " " + self.stud_data['surname'] + "\n" \
  + str(self.get_grades(group_id)) + "\n" +str(self.get_attendances(group_id)) + "\n"

 def get_grades(self,group_id):
  grades = str(self.stud_data['grades'][group_id])
  if len(self.stud_data['grades'][group_id]) != 0:
   grades += " avg: " + str(float(sum(self.stud_data['grades'][group_id]))/float(len(self.stud_data['grades'][group_id])))
  return grades

 def get_attendances(self,group_id):
  attendances = str(self.stud_data['attendances'][group_id])
  if len(self.stud_data['attendances'][group_id]) != 0:
   attendances += " present: " + str(float(sum(self.stud_data['attendances'][group_id]))/float(len(self.stud_data['attendances'][group_id]))) + "%"
  return attendances


class Group(object):
 def __init__(self,students_list,group_name,group_id):
  self.stud_list = students_list
  self.group_name = group_name
  self.group_id = group_id

 def Lesson(self):
  for student in self.stud_list:
   is_present = randrange(0,2)
   student.stud_data['attendances'][self.group_id].append(is_present)
   student.stud_data['grades'][self.group_id].append(randrange(0,3)*is_present+3)

 def __str__(self):
  group =  str(self.group_name) + " " + str(self.group_id) + "\n"
  for stud in self.stud_list:
   group += stud.print_stud(self.group_id)
  return group
 
 def assign_student(self,student):
  self.stud_list.append(student)


class Highschool(object):
 def __init__(self,stud_list,group_list):
  self.stud_list = stud_list
  self.group_list = group_list
  self.assign_students()

 def assign_students(self):
  for group in self.group_list:
   for student in self.stud_list:
    if group.group_id in student.lectures_id:
     group.assign_student(student)


if __name__ == '__main__':
 stud = []
 grupa = []
 stud.append(Student('Marian','Mariański',[0,3,4]))
 stud.append(Student('Marian','Marianiak',[0,1,2]))
 stud.append(Student('Marian','Marianowicz',[1,2,3,4]))
 stud.append(Student('Marian','Marian',[0,2,3,4]))
 stud.append(Student('Marian','Marianicz',[2,3,4]))
 stud.append(Student('Marian','Maryjan',[0,1,2,3,4]))
 grupa.append(Group([],"math",0))
 grupa.append(Group([],"astrophisics",1))
 grupa.append(Group([],"phisics",2))
 grupa.append(Group([],"history",3))
 grupa.append(Group([],"astrohistory",4))

 school = Highschool(stud,grupa)

 for i in range(20):
  for group in school.group_list:
   group.Lesson()
 for group in school.group_list:
  print (group)

# print("aa")
# print(Student('Marian','Marianski',[0,3,4]).__dict__)
