import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Miriam','pswd4363')

	def test__init__(self):
		'''
		Test to if check the initialization of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'Miriam')
		self.assertEqual(self.new_user.password,'pswd4363')

