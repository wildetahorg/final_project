from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    browser.implicitly_wait(10)

    page = MainPage(browser,link) #intialise Page Object, add browser.driver example and url

    page.open() 
    page.go_to_login_page()