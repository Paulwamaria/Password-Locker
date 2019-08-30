import unittest
from user import User
class TestUser(unittest.TestCase):

  def setUp(self):
    self.new_user = User("Paul", "Wamaria", "0780404626", "helloemryon@gmail.com","leejones1")

  def test_init(self):
    self.assertEqual(self.new_user.first_name,"Paul")
    self.assertEqual(self.new_user.last_name,"Wamaria")
    self.assertEqual(self.new_user.phone_number,"0780404626")
    self.assertEqual(self.new_user.email_address,"helloemryon@gmail.com")
    self.assertEqual(self.new_user.password, "leejones1")


if __name__=='__main__':
  unittest.main()
