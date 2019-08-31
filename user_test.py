import unittest
from user import User
from credentials import Credentials
class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Paul", "Wamaria", "0780404626", "helloemryon@gmail.com", "Paulwamaria", "leejones1")

    def test_init(self):
        self.assertEqual(self.new_user.first_name,"Paul")
        self.assertEqual(self.new_user.last_name,"Wamaria")
        self.assertEqual(self.new_user.phone_number,"0780404626")
        self.assertEqual(self.new_user.email_address,"helloemryon@gmail.com")
        self.assertEqual(self.new_user.username, "Paulwamaria")
        self.assertEqual(self.new_user.password, "leejones1")



    def tearDown(self):
        User.users_list = []

    def test_save_multiple_userDetails(self):
        self.new_user.save_userDetails()
        test_user = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")
    def test_check_if_userExist(self):

        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user
        test_user.save_userDetails()
        self.assertEqual(len(User.users_list),2)


# testing credentials
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials("twitter", "Just Paul","@Paulenigmatico", "paulwamaria@gmail.com","leejones1")

    def test_init(self):
        self.assertEqual(self.new_credential.account_type,"twitter")
        self.assertEqual(self.new_credential.registration_name,"Just Paul")
        self.assertEqual(self.new_credential.username,"@Paulenigmatico")
        self.assertEqual(self.new_credential.registration_email,"paulwamaria@gmail.com")
        self.assertEqual(self.new_credential.account_password, "leejones1")

    def test_check_if_userExist(self):
        '''
        A test function to ensure the working of the check if userExist function.
        '''
        self.new_user = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")
        self.new_user.save_userDetails()

        user2 = User("test","user","0780404626","helloemryon@gmail.com","Pwamaria","leejones1")

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.first_name
        return current_user


    def test_save_credentials(self):

        '''
        A funtion to check if the method save_credentials is saving the new credenntials as expected.
        '''
        
        self.new_credential.save_credentials()
        twitter = Credentials("twitter", "Just Paul","@Paulenigmatico", "paulwamaria@gmail.com","leejones2" )
        twitter.save_credentials()

        self.assertEqual(len(Credentials.credentials_list), 2)



if __name__=='__main__':
  unittest.main()
