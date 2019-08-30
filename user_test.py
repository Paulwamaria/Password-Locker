import unittest
from user import User
from credentials import Credentials
class TestUser(unittest.TestCase):

  def setUp(self):
    self.new_user = User("Paul", "Wamaria", "0780404626", "helloemryon@gmail.com","leejones1")

  def test_init(self):
    self.assertEqual(self.new_user.first_name,"Paul")
    self.assertEqual(self.new_user.last_name,"Wamaria")
    self.assertEqual(self.new_user.phone_number,"0780404626")
    self.assertEqual(self.new_user.email_address,"helloemryon@gmail.com")
    self.assertEqual(self.new_user.password, "leejones1")

  def test_save_userDetails(self):
    self.new_user.save_userDetails()
    self.assertEqual(len(User.user_list),1)


# testing credentials
class TestCredentials(unittest.TestCase):
  def setUp(self):
    self.new_credentials = Credentials("twitter","Just Paul","@Paulenigmatico","paulwamaria@gmail.com","lee1")

  def test_init(self):
    self.assertEqual(self.new_credentials.account_type,"twitter")
    self.assertEqual(self.new_credentials.registration_name,"Just Paul")
    self.assertEqual(self.new_credentials.username,"@Paulenigmatico")
    self.assertEqual(self.new_credentials.registration_email,"paulwamaria@gmail.com")
    self.assertEqual(self.new_credentials.account_password, "lee1")

if __name__=='__main__':
  unittest.main()
