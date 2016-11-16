import unittest
from group import *
from kol2_gr import * 
from student import * 

class Diary_Tester(unittest.TestCase):
	def setUp(self):
		self.diary = group()
	def test_add_student(self):
		self.assertEqual("Added",self.diary.add_student(student("Ala","Makota"))
	def test_check_attendance(self):
		self.assertEqual(4.25,self.avg_grade())
	#def test_check_attendance(self):
	#	self.assertEqual()
	# rest tests in progress ... source not compilable at all


if __name__=="__main__"
	unittest.main()
