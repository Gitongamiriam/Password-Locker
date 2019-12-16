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

	def test_save_user(self):
    	'''
		Test to check if the new users info is saved 
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)
  
class TestCredentials(unittest.TestCase):
    '''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Miriam','pswd4363')
		self.new_user.save_user()
		user2 = User('philip','pswd4363')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))
