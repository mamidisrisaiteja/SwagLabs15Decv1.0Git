
from pytest_bdd import given,when,then,scenarios,parsers
from pages.login_page import LoginPage
import pytest
    
scenarios("login_page.feature")


# @pytest.fixture(scope="function")
# def login_page(page):
#     lp = LoginPage(page)
#     lp.open("https://www.saucedemo.com/")
#     return lp

       
@given("I am on the Login Page")
def I_am_on_the_Login_Page(login_page):
    pass
      
      
@when(parsers.parse("I login with username '{userName}' and password '{password}'"))
def I_login_with_username_and_password(login_page,userName,password):
       
    login_page.login_action(userName,password)
    

@then("I validate the page title")
def Then_I_validate_the_page_title(page):
    pass