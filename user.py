class User:
  user_list = []
  def __init__(self, first_name, last_name, phone_number, email_address, password):

    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email_address = email_address
    self.password = password

  def save_userDetails(self):
    User.user_list.append(self)