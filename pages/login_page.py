from .base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
   USERNAME="input#user-name"
   PASSWORD="//input[@placeholder='Username']"
   LOGIN_BTN="//input[@name='login-button']"

   def login_action(self,user_name,password):
  
        self.fill(self.USERNAME,user_name)
        self.fill(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)

   def open(self,base_url):
        self.goto(base_url)
   

