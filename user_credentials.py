import pyperclip
import random
import string

# Global Variables
global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	users_list = []
	def __init__(self,first_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.password = password
	def save_user(self):
    	'''
		Function to save a new user
		'''
		User.users_list.append(self)
  
class Credential:
    '''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user



