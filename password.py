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

def generate_password():
    '''
	Function to generate a password 
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
    '''
	Function to create a credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
    '''
	Function to save a credential
	'''
	Credential.save_credentials(credential)


