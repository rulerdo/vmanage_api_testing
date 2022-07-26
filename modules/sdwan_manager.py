import requests # Main module to send http requests
from urllib3.exceptions import InsecureRequestWarning # To avoid warnings on the terminal caused by http certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) # To avoid warnings on the terminal caused by http certificates

class sdwan_manager():

    def __init__(self):

        pass

    
    def get_auth_cookie(self):

        pass


    def get_auth_token(self):

        pass


    def logout(self):

        pass


    def send_get_request(self):

        pass

