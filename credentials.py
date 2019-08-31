from user import User
class Credentials:

    '''
    A class to hold the user's credentials, genrate passwords and also store the information
    '''
    
    credentials_list = []
    def __init__(self, account_type,registration_name, username, registration_email, account_password):
        self.account_type = account_type
        self.registration_name = registration_name
        self.username = username
        self.registration_email = registration_email
        self.account_password = account_password

@classmethod
def check_if_userExist(cls,username,password):

    '''
    A method to check if the user with the entered credentials exist
    '''

    current_user = " "
    for user in User.users_list:
        if user.username == userName and user.password == password:
            current_user = user.first_name
    return current_user