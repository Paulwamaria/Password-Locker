class Credentials:
  credentials_list = []
  def __init__(self, account_type,registration_name, username, registration_email, account_password):
    self.account_type = account_type
    self.registration_name = registration_name
    self.username = username
    self.registration_email = registration_email
    self.account_password = account_password