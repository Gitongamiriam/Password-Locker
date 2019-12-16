import pyperclip
from user_credentials import User, Credential

def create_user(fname,password):
	'''
	Function to create an account
	'''
	new_user = User(fname,password)
	return new_user

def save_user(user):
    '''
	Function to save anaccount
	'''
	User.save_user(user)
	
def verifing_user(first_name,password):
    '''
	Function that verifies an account before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user




