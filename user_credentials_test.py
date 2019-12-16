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
		Test to if check the initialization of user instances 
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
  
		Credential.credentials_list.append(self)
  
  	def setUp(self):
    	'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('Miriam','Facebook','gitongamiriam','pswd4363')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Miriam')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'gitongamiriam')
		self.assertEqual(self.new_credential.password,'pswd4363')

	def test_save_credentials(self):
		'''
  		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Gitonga','Twitter','Gitongamiriam','pswd4363')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)


	def tearDown(self):
    	'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []