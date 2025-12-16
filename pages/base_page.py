from playwright.sync_api import Page,expect

class BasePage:
    def __init__(self,page: Page):
        self.page=page
    
    def goto(self,url):
        self.page.goto(url)
    
    def fill(self,locator1,str1):
        self.page.fill(locator1,str1)

    def click(self,locator2):
        self.page.click(locator2)