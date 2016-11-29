import unittest
from random import randrange
from student import *

class test_student(unittest.TestCase):
	def setUp(self):
		self.stud_list = []
		self.group_list = []
		self.student = Student("Marian","Marianski",[0,3,4])
		self.stud_list.append(self.student)
		self.group = Group([],"math",0)
		self.group_list.append(self.group)
		self.school = Highschool(self.stud_list, self.group_list)

	def test_random_range(self):
		print(" Testowanie wartosci generatora liczb pseudolosowych ")
		self.assertTrue(randrange(0,2) >= 0 and randrange(0,2) <= 1)

	def test_grades_instance_of_str(self):
		print(" Sprawdzanie czy metoda get_grades() sprawdza odpowiedni komunikat ")
		self.assertIsInstance(self.student.get_grades(0), str)
		self.assertNotIsInstance(self.student.get_grades(0), int)

	def test_print_stud_instance_of_str(self):
		print(" Sprawdzanie czy metoda print_stud() sprawdza odpowiedni komunikat ")
		self.assertIsInstance(self.student.print_stud(0), str)
		self.assertNotIsInstance(self.student.print_stud(0), int)

	def test_attendances_instance_of_str(self):
		print(" Sprawdzanie czy metoda get_attendances() sprawdza odpowiedni komunikat ")
		self.assertIsInstance(self.student.get_attendances(0), str)
		self.assertNotIsInstance(self.student.get_attendances(0), int)

	def test_lectures_id(self):
		print(" Sprawdzanie uczestnictwa w wykladach ")
		self.assertEqual([0,3,4] ,self.student.lectures_id)

	def test_name_key_string(self):
		print(" Sprawdzanie poprawnosci kluczowania po imieniu ")
		self.assertEqual('Marian', self.student.stud_data['name'])
		self.assertNotEqual('Mariannnek', self.student.stud_data['name'])

	def test_surname_key_string(self):
		print(" Sprawdzanie poprawnosci kluczowania po imieniu ")
		self.assertEqual('Marianski', self.student.stud_data['surname'])
		self.assertNotEqual('Mariasasanski', self.student.stud_data['surname'])

	def test_empty_grades(self):
		print(" Sprawdzanie czy student nie ma poczatkowo ocen")
		self.assertNotIn([2,3,4,5], self.student.stud_data['grades'][0])

	def test_empty_attendances(self):
		print(" Sprawdzanie czy student nie ma poczatkowo uzupelnionych obecnosci")
		self.assertNotIn([0,1], self.student.stud_data['attendances'][0])

	def test_stud_class_instance(self):
		print(" Sprawdzanie czy obiekt jest instancja klasy Student")
		self.assertIsInstance(self.student, Student)

	def test_group_class_instance(self):
		print(" Sprawdzanie czy obiekt jest instancja klasy Student")
		self.assertIsInstance(self.group, Group)

	def test_str_overloading(self):
		print(" Sprawdzanie poprawnosci przeladowania __str__")
		self.assertIsInstance(self.group.__str__(), str)
		self.assertNotIsInstance(self.group.__str__(), int)

	def test_highschool_class_instance(self):
		print(" Sprawdzanie czy obiekt jest instancja klasy Highschool")
		self.assertIsInstance(self.school, Highschool)

	def test_stud_list_appending(self):
		print(" Sprawdzanie poprawnego dodania do listy studentow")
		self.assertIsNone(self.stud_list.append(Student("Marianna","Kowalska",[0,2,3])))

	def test_group_list_appending(self):
		print(" Sprawdzanie poprawnego dodania do listy grup")
		self.assertIsNone(self.group_list.append(Group([],"math",2)))

	def test_lectures_dict(self):
		print(" Sprawdzanie slownika przedmiotow")
		self.assertDictEqual({0:'maths',1:"astrophisics",2:"phisics",3:"history",4:"astrohistory"},lectures_available)

	def test_assign_student(self):
		print(" Sprawdzanie poprawnego przypisania studentow do grup")
		self.assertIsNone(self.group.stud_list.append(Student("Marianna","Kowalska",[0,2,3])))

if __name__ == '__main__':
	unittest.main()
