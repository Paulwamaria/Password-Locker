#!/usr/bin/env python3.6
import pyperclip
import string
import secret
import random
from credentials import credentials
from credentials import User

#Create a new user
def create_user(fname, lname, pnumber, eaddress, uname, pword):
    new_user = User(fname, lname, pnumber, eaddress, uname, pword)
    return new_user

#save contacts
def save_userDetails(contact):
    '''
    a funtion to save user details
    '''
    User.save_userDetails()


#Delete contact
def delete_contacts(contact):
    contact.delete_contact()