#!/usr/bin/env python3.6
import pyperclip
import string
import secret
import random
from credentials import credentials
from credentials import User

#Create a new user
def create_user(fname, lname, pnumber, eaddress, uname, pword):
    '''
    A funtcion to create a new user.
    '''
    new_user = User(fname, lname, pnumber, eaddress, uname, pword)
    return new_user

#save user
def save_userDetails(contact):
    '''
    a funtion to save user details
    '''
    User.save_userDetails()


#delete user
def delete_contacts(contact):
    '''
    A funtcion to delete a given user.
    '''
    contact.delete_contact()


def check_if_userExist(uname, pword):
    '''
    A function to return the user associated with the give password and username.
    '''
    return Credentials.check_if_userExist(uname, pword)

def generate_pword(pword_length):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credentials.generate_password(pword_length)

@classmethod
def display_credentials(cls,uname):
    '''
    A class method that displays all credentials of a given username.
    '''

    return cls.display_credentials(cls, uname)


@classmethod
def find_by_account_type(cls, account_site):
    '''
    A function to search for credentials when given an account site search as google, or twitter.
    '''
    return cls.find_by_account_type(cls, account_type)